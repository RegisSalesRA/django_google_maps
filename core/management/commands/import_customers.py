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
            with open(path, 'r') as customer_csv:
                reader = csv.reader(customer_csv)
                lista_customers = []
                for row in reader:
                    customer = Customers(
                    first_name = row[1],
                    last_name=row[2],
                    email=row[3],
                    gender=row[4],
                    company=row[5],
                    city=row[6],
                    title=row[7]
                )
                    lista_customers.append(customer)
                Customers.objects.bulk_create(lista_customers)    
            
        except Exception as error:
            print(f"Erro ao criar {error}")
        else:
            self.stdout.write("Csv has been imported successfully.")