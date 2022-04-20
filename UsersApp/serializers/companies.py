from rest_framework import serializers
from UsersApp.models.companies import Company
from UsersApp.utils import ObjectIdField

class CompanySerializer(serializers.ModelSerializer) :
    _id = ObjectIdField(read_only=True)

    class Meta:
        model= Company
        fields= '__all__' #('_id','name','state','creationDate')