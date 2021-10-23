from rest_framework import status
from rest_framework.test import APITestCase
from model_mommy import mommy
from core.models import Customer

class TestCustomer(APITestCase):
    endpoint_list_customers = "http://127.0.0.1:8000/api/v1/customers"
    endpoint_get_customer = "http://127.0.0.1:8000/api/v1/customers/1/"

    def setUp(self):
        self.customers = mommy.make(Customer)


    def test_list_customers(self):

        response = self.client.get(self.endpoint_list_customers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_customer(self):
         
        data =   {
           "id": 1,
            "first_name": self.customers.first_name,
            "last_name": self.customers.last_name,
            "email": self.customers.email,
            "gender": self.customers.gender,
            "company": self.customers.company,
            "city": self.customers.city,
            "title": self.customers.title,
            }

        response = self.client.get(self.endpoint_get_customer, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)