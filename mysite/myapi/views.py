from django.shortcuts import render
from myapi.models import Person
from rest_framework import viewsets
from .serializers import PersonSerializer
from rest_framework.views import APIView
from django.http import Http404



# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('userId')
    serializer_class = PersonSerializer

class PersonDetail(APIView):

    def get_object(self, pk):
        try:
            print("step", pk)
            return Person.objects.get(userId==pk)
        except Person.DoesNotExist:
            raise Http404




    

