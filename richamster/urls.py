from django.contrib import admin
from django.urls import path, include

from api.views import documentation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', documentation, name='documentation'),
    path('api/', include('api.urls')),
]
