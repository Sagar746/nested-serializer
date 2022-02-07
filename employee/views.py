from django.shortcuts import render

from rest_framework import generics
from .models import Employee,Bank 
from .serializers import EmployeeSerializer,BankSerializer

# Create your views here.


class EmployeeListCreateView(generics.ListCreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class = EmployeeSerializer


class BankListCreateView(generics.ListCreateAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer


class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer