from django.shortcuts import render

#REST FRAMEWORK
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

#SERIALIZER
from .serializers import CustomerSerializer

#MODEL
from .models import Customer


# Create your views here.

@api_view(["GET"])
def apiget(request,pk):
    customer = Customer.objects.get(id=pk)
    serializer = CustomerSerializer(customer, many=False)

    return Response(serializer.data)
    
@api_view(["GET"])
def apiall(request):
    customer = Customer.objects.all()
    serializer = CustomerSerializer(customer, many=True)

    return Response(serializer.data)

class CreateApi(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class UpdateApi(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DeleteApi(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer