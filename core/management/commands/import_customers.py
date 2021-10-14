from django.core.management.base import BaseCommand, CommandError
from core.models import Customers
from decouple import config
import csv

class Command(BaseCommand):
    help = "Load customers data into database from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("csv_customer_path", type=str)

    def handle(self, *args, **options):
        try:
            csv_customers = csv.DictReader(options["csv_customer_path"],)
            for csv_customer in csv_customers:
                customerlist = Customers.objects.create(**{
                    "first_name": csv_customer["first_name"],
                    "last_name":csv_customer["last_name"],
                    "email":csv_customer["email"],
                    "gender":csv_customer["gender"],
                    "company":csv_customer["company"],
                    "city":csv_customer["city"],
                    "title":csv_customer["title"]
                })
                customerlist.save()
                

        except Exception as error:
            print(f"Erro ao criar {error}")
        else:
            self.stdout.write("Csv has been imported successfully.")