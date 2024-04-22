from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from setup.views.department_view import DepartmentView
from setup.views.user_view import  UserView
from setup.views.item_view import DepartmentItemList, ItemView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()

router.register('items', ItemView, basename='Items')
router.register('departments', DepartmentView, basename='Departments')

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/', UserView.as_view()),
    path('api/users/<int:pk>',UserView.as_view()),
    path('api/users/<str:pk>',UserView.as_view()),
    path('api/departments/<int:pk>/items',DepartmentItemList.as_view()),
    path('api/login/', obtain_auth_token, name='login'),  
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]