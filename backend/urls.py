from django.contrib import admin
from todo import views                            # add this
from rest_framework import routers                    # add this
from django.urls import path                 # add this


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Task Management API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@abc.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# from django.urls import path  - DELETE THIS

urlpatterns = [
    path('admin/', admin.site.urls),
     path('todoapi/', views.TodoApi.as_view()),
    path('todoapi/<int:pk>', views.TodoApi.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

