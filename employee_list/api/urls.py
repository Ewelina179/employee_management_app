from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.authtoken import views

from employee_list.settings import (MEDIA_ROOT, MEDIA_URL)

from api.views import (CreateEmployeeView, CreateProfessionView,
                    DeleteEmployeeAjaxView, DeleteEmployeeView,
                    DeleteProfessionView, EmployeeListView, EmployeeView,
                    ProfessionListView, ReportFileView, ReportView,
                    UpdateEmployeeView, UpdateProfessionView, GetReportView, register)


from rest_framework import routers
from django.views.i18n import JavaScriptCatalog

from .views import EmployeeViewset, ProfessionViewSet

employees_router = routers.DefaultRouter()
employees_router.register("employees", viewset=EmployeeViewset, basename="employees")

profession_router = routers.DefaultRouter()
profession_router.register("professions", viewset=ProfessionViewSet, basename="professions")

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),
    path('api-token-auth/', views.obtain_auth_token),
    path('', EmployeeListView.as_view(), name='epmloyee_list_view'),
    path('employee/<pk>/details/', EmployeeView.as_view(), name='details'),
    path('employee/create/', CreateEmployeeView.as_view(), name='create'),
    path('employee/<pk>/edit/', UpdateEmployeeView.as_view(), name='update'),
    path('employee/<pk>/delete/', DeleteEmployeeView.as_view(), name='delete'),
    path('report/', ReportView.as_view(), name='url_for_report'),
    path('employee/<pk>/deleteajax/', DeleteEmployeeAjaxView.as_view(), name='delete_employee_ajax'),
    path('csv/', ReportFileView.as_view(), name='report'),
    path('profession/', ProfessionListView.as_view(), name='profession_list_view'),
    path('profession/create', CreateProfessionView.as_view(), name='create_profession'),
    path('profession/<pk>/edit/', UpdateProfessionView.as_view(), name='update_profession'),
    path('profession/<pk>/delete/', DeleteProfessionView.as_view(), name='delete_profession'),
    path('getreport/', GetReportView.as_view(), name='getreport' ),
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
