import graphene
from UsersApp.schemas import Query as queries
from UsersApp.schemas import Mutation as mutations

class Query(queries):
    pass

class Mutation(mutations):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)