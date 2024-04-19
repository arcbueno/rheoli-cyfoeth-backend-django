from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from setup.views.department_view import DepartmentView
from setup.views.user_view import  UserView
from setup.views.item_view import DepartmentItemList, ItemView

router = routers.DefaultRouter()

router.register('items', ItemView, basename='Items')
router.register('departments', DepartmentView, basename='Departments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', UserView.as_view()),
    path('api/users/<int:pk>',UserView.as_view()),
    path('api/users/<str:pk>',UserView.as_view()),
    path('api/departments/<int:pk>/items',DepartmentItemList.as_view()),
    path('api/login/', obtain_auth_token, name='login'),  
]