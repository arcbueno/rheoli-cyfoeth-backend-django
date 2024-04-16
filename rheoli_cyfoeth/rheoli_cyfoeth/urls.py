from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from setup.views.department_view import DepartmentView
from setup.views.employee_view import EmployeeView
from setup.views.item_view import DepartmentItemList, ItemView

router = routers.DefaultRouter()

router.register('employees', EmployeeView, basename='Employees')
router.register('items', ItemView, basename='Items')
router.register('departments', DepartmentView, basename='Departments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/departments/<int:pk>/items',DepartmentItemList.as_view()),
]