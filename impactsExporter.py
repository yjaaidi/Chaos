import os, sys, getopt, logging, csv
os.environ['CHAOS_CONFIG_FILE'] = "default_settings.py"
from chaos import db, utils, default_settings
from chaos.models import Export, Client

class impactsExporter:

    def __init__(self):
        self.logger = logging.getLogger('impacts exporter')

    def init_client_by_id(self, id):
        if not utils.is_uuid(id):
            raise ValueError("Wrong UUID format for client id")

        client = Client.query.get(id)
        if not client:
            raise ValueError("Wrong client id")

        self.client = client

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

    def check_required_arguments(self):
        if not self.client:
            raise ValueError("Client id should be provided")

        return True

    def get_client_impacts_between_application_dates(self, client_id, start_date, end_date):
        return Export.get_client_impacts_between_application_dates(client_id, start_date, end_date)

    def generate_file_path(self, item):
        datePattern = '%Y_%m_%d'
        start_date = item.start_date.strftime(datePattern)
        end_date = item.end_date.strftime(datePattern)

        fileName = '%s_impacts_export_%s_%s_%s.csv' % (self.client.client_code, start_date, end_date, item.id)
        filePath = os.path.join(default_settings.IMPACT_EXPORT_DIR, fileName)

        return os.path.abspath(filePath)

    def create_csv(self, filePath, impacts):
        with open(filePath, 'wb') as f:
            outcsv = csv.writer(f)
            outcsv.writerow(impacts.keys())
            outcsv.writerows(impacts.fetchall())
            f.close()

    def mark_export_as_done(self, item, filePath):
        if isinstance(item, Export):
            item.status = 'done'
            item.file_path = filePath
            item.updated_at = utils.get_current_time()
            db.session.commit()
            db.session.refresh(item)

    def mark_export_as_error(self, item):
        if isinstance(item, Export):
            item.status = 'error'
            item.updated_at = utils.get_current_time()
            db.session.commit()
            db.session.refresh(item)

    def run(self):
        try:
            item = None
            self.check_required_arguments()
            item = self.get_oldest_waiting_export(self.client.id)
            self.update_export_status(item, 'handling')
            impacts = self.get_client_impacts_between_application_dates(item.client_id, item.start_date, item.end_date)
            filePath = self.generate_file_path(item)
            self.create_csv(filePath, impacts)
            self.mark_export_as_done(item, filePath)
            self.logger.info('Impacts export for %s is available at %s' % (item.client_id, filePath))
        except UserWarning as w:
            self.mark_export_as_error(item)
            self.logger.info(w)
            sys.exit(0)
        except Exception as e:
            self.mark_export_as_error(item)
            self.logger.debug(e)
            sys.exit(1)

def get_command_arguments(argv):
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
    args = get_command_arguments(sys.argv[1:])

    exporter = impactsExporter()
    exporter.init_client_by_id(args['client_id'])
    exporter.run()
