from rest_framework import serializers
from scan.models import Employee,ROLES, CompanyOutlet,ActivityEmployee
from django.db import models
from django.contrib.auth.hashers import make_password

    


class RolesSerializer (serializers.ModelSerializer) :

     class Meta:
        model = ROLES
        fields = '__all__'


class EmployeesSerializer (serializers.ModelSerializer) :

     role = RolesSerializer(many=False, read_only=True)

     class Meta:
        model = Employee
        fields = ['id','username','email','role','status']
class EmployeesLoginSerializer (serializers.ModelSerializer):
    
     class Meta:
        model = Employee
        fields = ['password']


class EmployeesCreateSerializer (serializers.ModelSerializer):

      class Meta:
        model = Employee
        fields = ['username','email','password','company']
        extra_kwargs = {'password': {'write_only': True}}


      def create(self, validated_data):
       
        employee = Employee(**validated_data)
        print(validated_data.get('password'))
        employee.password = make_password(validated_data.get('password'))
        employee.save()
        return employee
class CompanyOutletSerializer (serializers.ModelSerializer):
    employees = EmployeesSerializer(many=True,read_only=True)
    class Meta:
        model = CompanyOutlet
        fields = '__all__'     
class EmployeesPostSerializer (serializers.ModelSerializer) :
     company = RolesSerializer(many=False, read_only=True)
     class Meta:
        model = Employee
        fields ='__all__'


class ActivityEmpDateSerializer (serializers.ModelSerializer):
   class Meta:
        model = ActivityEmployee
        fields = ["emp_id","date"]

class ActivityEmpSerializer (serializers.ModelSerializer):

    emp_id = EmployeesSerializer(
                many = False ,
                read_only = True
    )
    class Meta:
        model = ActivityEmployee
        fields = '__all__'

class ActivityPostEmpSerializer (serializers.ModelSerializer):

    class Meta:
        model = ActivityEmployee
        fields = ['emp_id','times','types']
