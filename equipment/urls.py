from django.urls import path
from equipment.views import (
    EquipmentList, EquipmentDetailView, CreateEquipment,
    UpdateEquipment, DeleteEquipment,
)

urlpatterns = [
    path('', EquipmentList.as_view(), name="equipment"),
    path('<int:pk>/', EquipmentDetailView.as_view(), name="equipment_view"),
    path('create/', CreateEquipment.as_view(), name="equipment_create"),
    path('<int:pk>/update/', UpdateEquipment.as_view(),
         name="equipment_update"),
    path('<int:pk>/delete/', DeleteEquipment.as_view(),
         name="equipment_delete"),
]
