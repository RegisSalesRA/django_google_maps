import csv
from core.models import Customers

with open('customers.csv', newline='') as csvfile:
    customers =  Customers.objects.create()
    reader = csv.DictReader(csvfile)
    for row in reader:
        customers(**{
            "first_name":row["first_name"],
            "last_name":row["last_name"],
            "email":row["email"],
            "gender":row["gender"],
            "company":row["company"],
            "city":row["city"],
            "title":row["title"]
        })
        customers.save()


with open('customers.csv', newline='') as csvfile:
    customers =  Customers.objects.create
    reader = csv.DictReader(csvfile)
    for row in reader:
        
            row["first_name"],
            row["last_name"],
            row["email"],
            row["gender"],
            row["company"],
            row["city"],
            row["title"]
    print(row)
