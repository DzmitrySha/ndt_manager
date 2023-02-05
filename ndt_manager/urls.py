from django.contrib import admin
from django.urls import path, include
# from ndt_manager import settings
from ndt_manager.views import IndexView, LoginUser, LogoutUser

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('equipment/', include('equipment.urls')),
    path('equiptypes/', include('equiptypes.urls')),
    path('stations/', include('stations.urls')),
    path('reports/', include('reports.urls')),
    path('certificates/', include('certificates.urls')),
    path('select2/', include('django_select2.urls')),
]
