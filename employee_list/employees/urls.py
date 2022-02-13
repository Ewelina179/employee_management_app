from django.conf.urls.static import static
from django.urls import path

from employee_list.settings.base import (DEBUG, MEDIA_ROOT, MEDIA_URL,
                                         STATIC_ROOT, STATIC_URL)

from . import views
from .views import (CreateEmployeeView, CreateProfessionView,
                    DeleteEmployeeAjaxView, DeleteEmployeeView,
                    DeleteProfessionView, EmployeeListView, EmployeeView,
                    ProfessionListView, ReportFileView, ReportView,
                    UpdateEmployeeView, UpdateProfessionView)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='epmloyee_list_view'),
    path('<pk>/details/', EmployeeView.as_view(), name='details'),
    path('create/', CreateEmployeeView.as_view(), name='create'),
    path('<pk>/edit/', UpdateEmployeeView.as_view(), name='update'),
    path('<pk>/delete/', DeleteEmployeeView.as_view(), name='delete'),
    path('report/', ReportView.as_view(), name='url_for_report'),
    path('<pk>/deleteajax/', DeleteEmployeeAjaxView.as_view(), name='delete_employee_ajax'),
    path('csv/', ReportFileView.as_view(), name='report'),
    path('professions/', ProfessionListView.as_view(), name='profession_list_view'),
    path('createprofession/', CreateProfessionView.as_view(), name='create_profession'),
    path('<pk>/editprofession/', UpdateProfessionView.as_view(), name='update_profession'),
    path('<pk>/deleteprofession/', DeleteProfessionView.as_view(), name='delete_profession')
]
urlpatterns += static(MEDIA_URL,document_root=MEDIA_ROOT)