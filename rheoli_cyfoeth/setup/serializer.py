from rest_framework import serializers

from setup.models.department import Department
from setup.models.item import Item
from django.contrib.auth.models import User

from setup.models.moving_history import MovingHistory

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
        
class DepartmentSerializer(serializers.ModelSerializer):
    manager = GetUserSerializer()
    
    class Meta:
        model= Department
        fields = '__all__'

class CreateDepartmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Department
        fields = ('name', 'description', 'manager')
        
class DepartmentItemListSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.description')
    class Meta:
        model = Item
        fields = '__all__'

class CreateMovingHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovingHistory
        fields = '__all__'
class CreateMovingHistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MovingHistory
        fields = ('finish_date', 'initial_department', 'destination_department', 'item_id', 'start_date')

class MovingHistorySerializer(serializers.ModelSerializer):
    initial_department = DepartmentSerializer()
    destination_department = DepartmentSerializer()
    
    class Meta:
        model = MovingHistory
        fields = '__all__'
        
class ItemSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    moving_history = MovingHistorySerializer(many=True)
    
    class Meta:
        model= Item
        fields = '__all__'
        read_only_fields = ('id', 'moving_history', 'department')
        