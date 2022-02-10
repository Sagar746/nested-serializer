from django.urls import path
from .views import EmployeeListCreateView,EmployeeRetrieveUpdateDestroyView
from .views import BankListCreateView,BankRetrieveUpdateDestroyView,RegisterAPIUser,LogoutAPIView
from .views import RegisterAPIUser


urlpatterns = [
	path('employee/create/', EmployeeListCreateView.as_view()),
	path('employee/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view()),
	path('bank/create/', BankListCreateView.as_view()),
	path('bank/<int:pk>/', BankRetrieveUpdateDestroyView.as_view()),

	path('register/', RegisterAPIUser.as_view()),
	path('logout/', LogoutAPIView.as_view()),
]