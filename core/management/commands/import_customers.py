from django.core.management.base import BaseCommand, CommandError
from core.models import Customers
import csv

class Command(BaseCommand):
    help = "Load customers data into database from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("csv_file_path", type=str)

    def handle(self, *args, **kwargs):
        try:
            path = kwargs['csv_file_path']
            with open(path, 'rt') as customer_csv:
                reader = csv.reader(customer_csv)
                for row in reader:
                    Customers.objects.create(**{
                    "first_name": row["first_name"],
                    "last_name":row["last_name"],
                    "email":row["email"],
                    "gender":row["gender"],
                    "company":row["company"],
                    "city":row["city"],
                    "title":row["title"]
                })             

        except Exception as error:
            print(f"Erro ao criar {error}")
        else:
            self.stdout.write("Csv has been imported successfully.")