from django.urls import *
from Item.models import Item, Photo
from Item.views import *

urlpatterns = [
    re_path(r'^$', IndexListView.as_view(), name='index'),
    re_path(r'^items/$', ItemListView.as_view(), name='items_list'),
    re_path(r'^items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='items_detail'),
    re_path(r'^photos/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photos_detail'),
]
