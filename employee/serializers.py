from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Employee,Bank

User=get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	password=serializers.CharField(required=True,write_only=True)
	password2=serializers.CharField(required=True,write_only=True)

	class Meta:
		model = User
		fields = ['username','email','password','password2']
		extra_kwargs={
			'password':{'write_only':True},
			'password2':{'write_only':True}
		}

	def create(self,validated_data):
		username=validated_data['username']
		email=validated_data['email']
		password=validated_data['password']
		password2=validated_data['password2']

		if password==password2:
			user = User(username=username,email=email)
			user.set_password(password)
			user.save()
			return user
		else:
			raise serializers.ValidationError({
				'error':'Both password do not match'
			})
		return super().create(validated_data)


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