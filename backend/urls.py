from django.contrib import admin
from todo import views                            # add this
from rest_framework import routers                    # add this
from django.urls import path, include                 # add this


router = routers.DefaultRouter()                      # add this
router.register(r'tasks', views.TodoView, 'task')     # add this


# from django.urls import path  - DELETE THIS

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),                # add this
]

