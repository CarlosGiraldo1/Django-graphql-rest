from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from bson.objectid import ObjectId

from UsersApp.models import Company
from UsersApp.serializers import CompanySerializer

@csrf_exempt
def companyApi(request, id=''): 

    if request.method == 'GET':
        # companies = Company.objects.all()
        # companies_serializer = CompanySerializer(companies, many=True)
        # return JsonResponse(companies_serializer.data, safe=False, status=200)


        if id == '' :
            try:
                companies = Company.objects.all()
            except:
                return JsonResponse('Server Error!', safe=False, status=500)
        else:
            try:
                companies = [Company.objects.get(_id=ObjectId(id))]
            except:
                return JsonResponse('Failed to update: _id not found!', safe=False, status=400)
        try:                    
            companies_serializer = CompanySerializer(companies, many=True)
            return JsonResponse(companies_serializer.data, safe=False, status=200)
        except: 
            return JsonResponse('Server Error!', safe=False, status=500)


    elif request.method == 'POST':
        try:
            companies_data = JSONParser().parse(request)
            companies_serializer = CompanySerializer(data=companies_data, many=True)
        except:
            return JsonResponse('Failed to Add, SyntaxError or empty request', safe=False, status=400)
        try:    
            if companies_serializer.is_valid(True):
                try:
                    companies_serializer.save()
                    return JsonResponse('Added Successfully', safe=False, status=200)
                except:
                    return JsonResponse('Failed to Add', safe=False, status=400)
            else:   
                return JsonResponse('Failed to Add', safe=False, status=400)
        except: 
            return JsonResponse('Failed to Add, incompleted required fields', safe=False, status=400)


    elif request.method == 'PUT':
        try:
            companies_data = JSONParser().parse(request)
            try:
                companies = Company.objects.get(_id=ObjectId(companies_data['_id']))
            except:
                return JsonResponse('Failed to update: _id not found!', safe=False) 
        except:
            return JsonResponse('Failed to update, SyntaxError or empty request', safe=False, status=400)

        try:             
            companies_serializer = CompanySerializer(companies)
            for k in companies_data:
                if k not in companies_serializer.data.keys():
                    return JsonResponse('Failed to update, SyntaxError or empty request', safe=False, status=400)
            for key in companies_serializer.data.keys():
                if key not in companies_data.keys():
                    companies_data[key] = companies_serializer.data[key]
            companies_serializer = CompanySerializer(companies, data=companies_data)
        except: 
            return JsonResponse('Failed to update', safe=False, status=400)
        try:
            if companies_serializer.is_valid():
                try:
                    companies_serializer.save()
                    return JsonResponse('Update Successfully', safe=False, status=200)
                except: 
                    return JsonResponse('Failed to update', safe=False, status=400)
            else: 
                return JsonResponse('Failed to update', safe=False, status=400)
        except: 
            return JsonResponse('Failed to update', safe=False, status=400)


    elif request.method == 'DELETE':
        if id == "":
            return JsonResponse('Failed to delete:Empty _id!', safe=False, status=400)
        else: 
            try:
                companies = Company.objects.get(_id=ObjectId(id))
            except: 
                return JsonResponse('Failed to delete: _id not found!', safe=False, status=400)  
            try:
                companies.delete()
                return JsonResponse('Deleted Successfully', safe=False, status=200)
            except: 
                return JsonResponse('Failed to delete', safe=False, status=400)

#companies = Company.objects.get(_id=ObjectId(companies_data['_id']))
