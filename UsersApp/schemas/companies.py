import graphene
import copy
from bson.objectid import ObjectId

from UsersApp.models import Company
from UsersApp.serializers import CompanySerializer
from UsersApp.types import *

#============================= Queries =====================================

class Query(graphene.ObjectType):
    all_companies = graphene.Field(CompanyResponseType)
    def resolve_all_companies(self, info, **kwargs):
        response = {}
        try:
            response['data'] = Company.objects.all()
            response['error'] = False
            response['status'] = 200
            response['message'] = "Successfull transaction!"
        except:
            response['data'] = []
            response['error'] = True
            response['status'] = 500
            response['message'] = "Server Error!"
        return response

    companyById = graphene.Field(CompanyResponseType, id=graphene.String())
    def resolve_companyById(self, info, id):
        response = {}
        if not(ObjectId.is_valid(id)):
            response['data'] = []
            response['error'] = True
            response['status'] = 400
            response['message'] = "Invalid id!"
        try:
            response['data'] = [Company.objects.get(_id=ObjectId(id))]
            response['error'] = False
            response['status'] = 200
            response['message'] = "Successfull transaction!"
        except:
            response['data'] = []
            response['error'] = True
            response['status'] = 400
            response['message'] = "Id not found!"
        return response

    companyExistsById = graphene.Field(CompanyExistsResponseType, id=graphene.String())
    def resolve_companyExistsById(self, info, id):
        response = {}
        if not(ObjectId.is_valid(id)):
            response['data'] = []
            response['error'] = True
            response['status'] = 400
            response['message'] = "Invalid id!"
        try:
            response['data'] = Company.objects.filter(_id=ObjectId(id)).exists()
            response['error'] = False
            response['status'] = 200
            response['message'] = "Successfull transaction!"
        except:
            response['data'] = []
            response['error'] = True
            response['status'] = 400
            response['message'] = "Id not found!"
        return response





#============================= Mutations =====================================

class CreateCompany(graphene.Mutation):
    class Arguments:
        input = graphene.List(CompanyInputCreate)

    company = graphene.List(CompanyType)

    def mutate(self, info, input):
        company_serializer = CompanySerializer(data=input, many=True)
        if company_serializer.is_valid():
            resp = company_serializer.save()
            return CreateCompany(company=resp)

class UpdateCompany(graphene.Mutation):
    class Arguments:
        input = CompanyInput(required=True)

    data = graphene.List(CompanyType)
    data_old = graphene.List(CompanyType)
    error = graphene.Boolean()
    message = graphene.String()
    status = graphene.Int()

    def mutate(self, info, input):
        data = Company.objects.get(_id=ObjectId(input['id']))
        data_old = copy.deepcopy(data)
        company_serializer = CompanySerializer(data, data=input)
        if company_serializer.is_valid():
            company_serializer.save()
            return UpdateCompany(error=False, message= "Updated Successfully", status=200 ,data=[data],data_old=[data_old])
        return UpdateCompany(error=True, message= "Failed to update!", status=400 ,data=[],data_old=[])

class DeleteCompany(graphene.Mutation):
    class Arguments:
        id = graphene.String()

    company = graphene.String()

    def mutate(self, info, id):
        company_selected = Company.objects.get(_id=ObjectId(id))
        company_selected.delete()
        return DeleteCompany(company="Deleted Successfully")

class Mutation(graphene.ObjectType):
    update_company = UpdateCompany.Field()
    create_company = CreateCompany.Field()
    delete_company = DeleteCompany.Field()