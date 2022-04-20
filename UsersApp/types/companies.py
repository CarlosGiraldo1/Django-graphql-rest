import graphene
from graphene_django.types import DjangoObjectType

from UsersApp.models import Company

#===================================== ObjectType ============================================
class CompanyType(DjangoObjectType):
    class Meta:
        model = Company
        fields = ('_id','name','state','creationDate')
        
class CompanyResponseType(graphene.ObjectType):
    error = graphene.Boolean()
    message = graphene.String()
    status = graphene.Int()
    data = graphene.List(CompanyType)

class CompanyExistsResponseType(graphene.ObjectType):
    error = graphene.Boolean()
    message = graphene.String()
    status = graphene.Int()
    data = graphene.Boolean()


#===================================== InputType ============================================


class CompanyInputCreate(graphene.InputObjectType):
    name = graphene.String()

class CompanyInput(graphene.InputObjectType):
    id = graphene.String()
    name = graphene.String()
    state = graphene.Int()