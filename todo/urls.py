
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core import views


router = DefaultRouter()

router.register('todo', views.TotoIt)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls'))
]
