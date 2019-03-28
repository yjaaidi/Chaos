import os, sys, getopt, logging, csv
os.environ['CHAOS_CONFIG_FILE'] = "default_settings.py"
from chaos import db, utils, default_settings
from chaos.models import Export, Client

class impactsExporter:

    def setclientId(self, id):
        self.clientId = id
        self.logger = logging.getLogger('impacts exporter')

    def get_oldest_waiting_export(self, clientId):
        item = Export.get_oldest_waiting_export(clientId)
        if not item:
            raise UserWarning("No waiting task for this client has been found")

        return item

    def update_export_status(self, item, status):
        item.status = status
        item.process_start_date = utils.get_current_time()
        item.updated_at = utils.get_current_time()
        db.session.commit()
        db.session.refresh(item)

    def checkRequiredArguments(self):
        if not self.clientId:
            raise ValueError("Client id should be provided")

        if not utils.is_uuid(self.clientId):
            raise ValueError("Wrong UUID format for client id")

        client = Client.query.get(self.clientId)
        if not client:
            raise ValueError("Wrong client id")
        return True

    def getArchivedImpacts(self, client_id, start_date, end_date):
        return Export.getArchivedImpacts(client_id, start_date, end_date)

    def generateFilePath(self, prefix):
        fileName = os.path.join(default_settings.IMPACT_EXPORT_DIR, prefix + '.csv')
        return os.path.abspath(fileName)

    def createCSV(self, filePath, impacts):
        with open(filePath, 'wb') as f:
            outcsv = csv.writer(f)
            outcsv.writerow(impacts.keys())
            outcsv.writerows(impacts.fetchall())
            f.close()

    def markExportAsDone(self, item, filePath):
        item.status = 'done'
        item.file_path = filePath
        item.updated_at = utils.get_current_time()
        db.session.commit()
        db.session.refresh(item)

    def run(self):
        try:
            self.checkRequiredArguments()
            item = self.get_oldest_waiting_export(self.clientId)
            self.update_export_status(item, 'handling')
            impacts = self.getArchivedImpacts(item.client_id, item.start_date, item.end_date)
            filePath = self.generateFilePath(item.id)
            self.createCSV(filePath, impacts)
            self.markExportAsDone(item, filePath)
            self.logger.info('Impacts are exported in ' + filePath)
        except UserWarning as w:
            self.logger.info(w)
            sys.exit(0)
        except Exception as e:
            self.logger.debug(e)
            sys.exit(1)

def getCommandArguments(argv):
    client_id = ''
    opts, args = getopt.getopt(argv,"hc:",["client_id=",])

    for opt, arg in opts:
        if opt == '-h':
            print 'impactsExporter.py -c <client_id>'
            sys.exit()
        elif opt  == '-c':
            client_id = arg

    return {'client_id': client_id }


if __name__ == "__main__":
    args = getCommandArguments(sys.argv[1:])

    exporter = impactsExporter()
    exporter.setclientId(args['client_id'])
    exporter.run()
