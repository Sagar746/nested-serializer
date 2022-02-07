from django.db import models

# Create your models here.

class BaseModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True



class Employee(BaseModel):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	email = models.CharField(max_length=255, unique=True)
	phone = models.CharField(max_length=15)

	def __str__(self):
		return self.name


class Bank(BaseModel):
	employee = models.ForeignKey(Employee,null=True,on_delete=models.CASCADE,related_name='banks')
	account_no = models.CharField(max_length=50)
	bank_name = models.CharField(max_length=50)