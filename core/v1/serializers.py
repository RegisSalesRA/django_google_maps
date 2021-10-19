
from django.db import models
from django.db.models import fields
from rest_framework import serializers;
from core.models import Customer

class CustomerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            'id','first_name','last_name','email','gender','company','city','title','longitude','latitude'
        )
