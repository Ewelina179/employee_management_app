from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api.urls import employees_router, profession_router

handler400 = 'api.views.handler400'
handler404 = 'api.views.handler404'
handler500 = 'api.views.handler500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('', include(profession_router.urls)),
    path('', include(employees_router.urls))
]
