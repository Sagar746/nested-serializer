from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics
from .models import Employee,Bank 
from .serializers import EmployeeSerializer,BankSerializer,CreateUserSerializer

# Create your views here.

class RegisterUser(APIView):
	def post(self,request):
		serializer = CreateUserSerializer(data=request.data)

		if not serializer.is_valid():
			return Response({'status':403,'errors':serializer.errors})
		serializer.save()
		user=User.objects.get(username=serializer.data['username'])
		token_obj, _ = Token.objects.get_or_create(user=user)
		return Response({'status':200, 'payload':serializer.data})

class EmployeeListCreateView(generics.ListCreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	permission_classes = [IsAuthenticated,]
	authentication_classes = [TokenAuthentication,]

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class = EmployeeSerializer


class BankListCreateView(generics.ListCreateAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer


class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer