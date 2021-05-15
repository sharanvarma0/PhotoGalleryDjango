from django.urls import *
from django.contrib import admin


urlpatterns = [
    re_path(r'^admin/',admin.site.urls),
    re_path(r'^', include('Item.urls')),
]
