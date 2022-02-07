from django.urls import path
from . import views
from employee_list.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from .views import EmployeeView, CreateEmployeeView, UpdateEmployeeView, DeleteEmployeeView

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<pk>/details/', EmployeeView.as_view()),
    path('create/', CreateEmployeeView.as_view()),
    path('<pk>/edit/', UpdateEmployeeView.as_view()),
    path('<pk>/delete/', DeleteEmployeeView.as_view()),
]