from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

#Rest Framework (third parties)
from rest_framework.response import Response
from rest_framework.views import APIView

class TestView(APIView):
    def get(self,request,*args,**kwargs):
        data = {
            'name' : 'Pankaj',
            'age' : 25
        }
        return Response(data)


