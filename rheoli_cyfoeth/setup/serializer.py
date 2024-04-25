from rest_framework import serializers

from setup.models.department import Department
from setup.models.item import Item
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'first_name', 'last_name']
        read_only_fields = ('id',)

class CreateUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'first_name', 'last_name', 'password']
        write_only_fields = ('password',)
        read_only_fields = ('id',)
class GetUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'first_name', 'last_name', ]
        

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    manager = GetUserSerializer()
    
    class Meta:
        model= Department
        fields = '__all__'
        
class DepartmentItemListSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.description')
    class Meta:
        model = Item
        fields = '__all__'
    