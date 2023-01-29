from django.urls import path

from equiptypes.views import (EquipTypesList, CreateEquipType,
                              UpdateEquipType, DeleteEquipType)

urlpatterns = [
    path('', EquipTypesList.as_view(), name="equiptypes"),
    path('create/', CreateEquipType.as_view(), name="equiptype_create"),
    path('<int:pk>/update/', UpdateEquipType.as_view(),
         name="equiptype_update"),
    path('<int:pk>/delete/', DeleteEquipType.as_view(),
         name="equiptype_delete"),
]
