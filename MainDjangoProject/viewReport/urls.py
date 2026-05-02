from django.urls import path
from . import views

urlpatterns = [
    path("", views.addViewReportPage, name="add_view_report_page")
]