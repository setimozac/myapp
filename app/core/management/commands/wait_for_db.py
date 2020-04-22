from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections
import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('waiting for db...')
                time.sleep(1)
        self.stdout.write('database is available')
