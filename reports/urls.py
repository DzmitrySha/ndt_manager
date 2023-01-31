from django.urls import path

from reports.views import (ReportsList, CreateReport,
                           UpdateReport, DeleteReport)

urlpatterns = [
    path('', ReportsList.as_view(), name="reports"),
    path('create/', CreateReport.as_view(), name="report_create"),
    path('<int:pk>/update/', UpdateReport.as_view(), name="report_update"),
    path('<int:pk>/delete/', DeleteReport.as_view(), name="report_delete"),
]
