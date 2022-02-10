from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from .models import Employee,Bank 
from .serializers import EmployeeSerializer,BankSerializer,UserRegisterSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

class RegisterAPIUser(APIView):
	serializer_class=UserRegisterSerializer
	def post(self,request,format=None):
		serializer=self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		user=serializer.save()
		refresh=RefreshToken.for_user(user)
		response_data={
			'refresh':str(refresh),
			'access':str(refresh.access_token),
		}
		return Response({'payload':serializer.data})

class LogoutAPIView(APIView):
	def post(self,request,format=None):
		try:
			token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
			token_obj = RefreshToken(token)
			token_obj.blacklist()
			return Response(status=status.HTTP_200_OK)
		except Exception as e:
			return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeeListCreateView(generics.ListCreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	permission_classes = [IsAuthenticated,]
	authentication_classes = [JWTAuthentication,]

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset=Employee.objects.all()
	serializer_class = EmployeeSerializer


class BankListCreateView(generics.ListCreateAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer


class BankRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Bank.objects.all()
	serializer_class = BankSerializer