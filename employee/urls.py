from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import EmployeeListCreateView,EmployeeRetrieveUpdateDestroyView
from .views import BankListCreateView,BankRetrieveUpdateDestroyView,RegisterUser


urlpatterns = [
	path('employee/create/', EmployeeListCreateView.as_view()),
	path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view()),
	path('bank/create/', BankListCreateView.as_view()),
	path('bank/<int:pk>/', BankRetrieveUpdateDestroyView.as_view()),

	path('login/', obtain_auth_token),
	path('register/',RegisterUser.as_view()),
]