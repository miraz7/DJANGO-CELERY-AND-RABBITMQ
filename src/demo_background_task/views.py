from re import A
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Main.settings.celery import app as celery_app



@celery_app.task(name='print-list')
def  list_print_function(l):
    print(l)



# Create your views here.
class CreateBackgroundTask (APIView):
    def get(self , request,  *args, **kwargs):

        list  = [
            {
                'name' : "A",
                'sub' : "b"
            },
            {
                'name' : "C",
                'sub' : "D"
            },
            {
                'name' : "E",
                'sub' : "F"
            },
            {
                'name' : "G",
                'sub' : "H"
            }
        ]

        for l in list :

            list_print_function.delay(l = l)

        return Response({'data': 'sales_eport'}, status=status.HTTP_200_OK)
        
