from django.urls import path
from . import views
from employee_list.settings.base import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import EmployeeListView, EmployeeView, CreateEmployeeView, UpdateEmployeeView, DeleteEmployeeView, ReportView, DeleteView

urlpatterns = [
    path('', EmployeeListView.as_view(), name='epmloyee_list_view'),
    path('<pk>/details/', EmployeeView.as_view()),
    path('create/', CreateEmployeeView.as_view()),
    path('<pk>/edit/', UpdateEmployeeView.as_view()),
    path('<pk>/delete/', DeleteEmployeeView.as_view()),
    path('report/', ReportView.as_view()),
    path('delete/', DeleteView.as_view()),
    path('csv/',views.getfile, name='report')  
]