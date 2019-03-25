import os, sys, getopt
os.environ['CHAOS_CONFIG_FILE'] = "default_settings.py"
import logging
from chaos import db
from chaos.models import Export

class impactsExporter:


    clientCode = ''

    def setClientCode(self, code):
        self.clientCode = code

    def get_oldest_waiting_export(self):
        return Export.get_oldest_waiting_export()

    def update_export_status(self, item, status):
        item.status = status
        db.session.commit()
        db.session.refresh(item)

    def checkRequiredArguments(self):
        if not self.clientCode:
            raise ValueError("Client code should be provided")
        return True

    def run(self):
        try:
            self.checkRequiredArguments()
            item = self.get_oldest_waiting_export()
            self.update_export_status(item, 'handling')
        except Exception as e:
            logging.getLogger(__name__).debug(e)
            sys.exit(2)

def getCommandArguments(argv):
    client_code = ''
    opts, args = getopt.getopt(argv,"hc:",["client_code=",])

    for opt, arg in opts:
        if opt == '-h':
            print 'impactsExporter.py -c <client_code>'
            sys.exit()
        elif opt  == '-c':
            client_code = arg

    return {'client_code': client_code }

if __name__ == "__main__":
    args = getCommandArguments(sys.argv[1:])

    exporter = impactsExporter()
    exporter.setClientCode(args['client_code'])
    exporter.run()