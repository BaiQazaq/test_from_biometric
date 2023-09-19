from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from django.shortcuts import render
from datetime import datetime
# from rest_framework.pagination import LimitOffsetPagination
from django.core.paginator import Paginator
from web_app.models import People
from web_app.serializer import PeopleSerializer

class PeopleView(APIView):

    def get(self, request, **kwargs):
        inn = kwargs.get("pk", None)
        inn = str(inn)
        if len(inn) < 12:
            try:
                people = People.objects.all().exclude(is_deleted = True)
                
                page_number = self.request.query_params.get('page_number', 1)
                page_size = self.request.query_params.get('page_size', 10)
                paginator = Paginator(people, page_size)

                serializer = PeopleSerializer(paginator.page(page_number), many=True, context={'request':request})

                return Response(serializer.data, status=200)
            except Exception as e:
                error = type(e).__name__
                print(error)
        elif len(inn) == 12:  
            try:
                person = People.objects.get(inn=inn)
                serializer = PeopleSerializer(person)
                return Response(serializer.data, status=200)

            except Exception as e:
                return Response({"error": "Object does not exists"})
        else:
            print('Somthing wrong')
    
    @staticmethod
    def age_count (inn):
        born_year_str = inn[0:2]
        born_year = int(born_year_str)
        current_year = int(datetime.now().year)
        age = current_year - born_year
        if age > 2000:
            age = age - 2000
        elif 1900 < age < 2000:
            age = age - 1900
        return age

    def post (self, request):
        age = PeopleView.age_count(request.data['inn'])
        new_man = People.objects.create(
            name = request.data['name'],
            inn = request.data['inn'],
            age = age
        )
       
        return Response({'post': model_to_dict(new_man)})
    
    
    def patch(self, request, *args, **kwargs):
        inn = kwargs.get("pk", None)
        inn = str(inn)
        if not inn:
            return Response({"error": "Method PATCH not allowed"})
        
        try:
            
            instance = People.objects.get(inn=inn)
            print("INSTANCE",instance)
            print("REQUEST+++", request.data)
        except:
            return Response({"error": "Object does not exists"})
        print("+"*5, request.data)
        serializer = PeopleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"post": serializer.data}, status=200)

    
    def delete(self, request, *args, **kwargs):
        inn = kwargs.get("pk", None)
        inn = str(inn)
        if not inn:
            return Response({"error": "Method DELETE not allowed"})
        try:
            person = People.objects.get(inn = inn)
            serializer = PeopleSerializer(data=person.__dict__)
            print("DELETE", person, "+++++", serializer)
            if serializer.is_valid():
                person.delete()
                return Response(person.inn, status=204)
        except:
            return Response(serializer.errors, status=400)
        
    

        