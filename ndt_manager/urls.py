from django.contrib import admin
from django.urls import path, include
# from ndt_manager import settings
from ndt_manager.views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('equipment/', include('equipment.urls')),
]
