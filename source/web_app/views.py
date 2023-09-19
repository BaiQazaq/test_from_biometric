from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from django.shortcuts import render
from datetime import datetime
from web_app.models import People
from web_app.serializer import PeopleSerializer

# Create your views here.

class PeopleView(APIView):

    def get(self, request):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        print("++++++++++",serializer)
        return Response(serializer.data)
    
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
    

        