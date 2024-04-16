from rest_framework import serializers

from setup.models.department import Department
from setup.models.employee import Employee
from setup.models.item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = '__all__'
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields = '__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields = ['id', 'name']
        
class DepartmentItemListSerializer(serializers.ModelSerializer):
    department = serializers.ReadOnlyField(source='department.description')
    class Meta:
        model = Item
        fields = '__all__'
    