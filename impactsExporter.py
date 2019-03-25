import os
os.environ['CHAOS_CONFIG_FILE'] = "default_settings.py"
from chaos import db
from chaos.models import Export

class impactsExporter:

    def get_oldest_waiting_export(self):
        return Export.get_oldest_waiting_export()

    def update_export_status(self, item, status):
        item.status = status
        db.session.commit()
        db.session.refresh(item)

    def run(self):
        item = self.get_oldest_waiting_export()
        self.update_export_status(item, 'handling')


if __name__ == "__main__":
    exporter = impactsExporter()
    exporter.run()