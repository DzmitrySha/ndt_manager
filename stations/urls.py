from django.urls import path

from stations.views import (StationsList, CreateStation,
                            UpdateStation, DeleteStation)

urlpatterns = [
    path('', StationsList.as_view(), name="stations"),
    path('create/', CreateStation.as_view(), name="station_create"),
    path('<int:pk>/update/', UpdateStation.as_view(), name="station_update"),
    path('<int:pk>/delete/', DeleteStation.as_view(), name="station_delete"),
]
