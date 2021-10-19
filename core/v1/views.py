from core.v1.serializers import CustomerSerializers
from core.models import Customer
from rest_framework.views import APIView
from rest_framework import generics

class CustomerViews(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers


class CustomerViewsCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers