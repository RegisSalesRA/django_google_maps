from django.core.management.base import BaseCommand, CommandError
from core.models import Customer
import csv
import requests
class Command(BaseCommand):
    help = "Load Customer data into database from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("csv_file_path", type=str)

    def handle(self, *args, **kwargs):
        try:
            path = kwargs['csv_file_path']
            with open(path, 'r') as customer_csv:
                reader = csv.reader(customer_csv)
                next(reader, None) 
                lista_Customer = []
                for row in reader:
                    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={row[6]}&key=<KeyGoogleApi>')
                    resp_json_payload = response.json()

                    customer = Customer(**{
                    "first_name": row[1],
                    "last_name":row[2],
                    "email":row[3],
                    "gender":row[4],
                    "company":row[5],
                    "city":row[6],
                    "title":row[7]
                    })
                
                    if resp_json_payload['status'] == 'OK':
                        customer.latitude = resp_json_payload['results'][0]['geometry']['location']['lat']
                        customer.longitude = resp_json_payload['results'][0]['geometry']['location']['lng']
                                               
                
                    lista_Customer.append(customer)
                Customer.objects.bulk_create(lista_Customer)    
            
        except Exception as error:
            print(error)
        else:
            self.stdout.write("Csv has been imported successfully.")