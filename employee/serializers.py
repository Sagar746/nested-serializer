from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Employee,Bank


class CreateUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username','email','password']

class BankSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Bank
		fields=['account_no','bank_name']
	



class EmployeeSerializer(serializers.ModelSerializer):

	banks = BankSerializer(many=True)
	class Meta:
		model = Employee
		fields = ['name','address','email','phone','banks']



	def create(self, validated_data):
		banks_data = validated_data.pop('banks')
		employee   = Employee.objects.create(**validated_data)
		for bank in banks_data:
			Bank.objects.create(employee=employee, **bank)
		return employee



	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.address = validated_data.get('address', instance.address)
		instance.email = validated_data.get('email', instance.email)
		instance.phone = validated_data.get('phone', instance.phone)
		instance.save()

		banks = validated_data.get('banks')

		for bank in banks:
			bank_id = bank.get('id', None)
			if bank_id:
				inv_bank = Bank.objects.get(id=bank_id, employee=instance)
				inv_bank.name = bank.get('name', inv_bank.name)
				inv_bank.price = bank.get('price', inv_bank.price)
				inv_bank.save()
			else:
				Bank.objects.create(employee=instance, **bank)

		return instance