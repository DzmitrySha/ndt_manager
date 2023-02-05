from django.urls import path

from certificates.views import (CertificatesList, CreateCertificate,
                                UpdateCertificate, DeleteCertificate)

urlpatterns = [
    path('', CertificatesList.as_view(), name="certificates"),
    path('create/', CreateCertificate.as_view(), name="certificate_create"),
    path('<int:pk>/update/', UpdateCertificate.as_view(),
         name="certificate_update"),
    path('<int:pk>/delete/', DeleteCertificate.as_view(),
         name="certificate_delete"),
]
