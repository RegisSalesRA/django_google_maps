import csv

class Customer():
    def __init__(self,first_name
    ,last_name,email,gender,company,city,title
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.company = company
        self.city = city
        self.title = title

with open('customers.csv', newline='') as csvfile:
    list_customers = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        custumer = Customer(**{
            "first_name": row["first_name"],
            "last_name":row["last_name"],
            "email":row["email"],
            "gender":row["gender"],
            "company":row["company"],
            "city":row["city"],
            "title":row["title"]
        })
        list_customers.append(row)
    print(list_customers)
    print(len(list_customers))