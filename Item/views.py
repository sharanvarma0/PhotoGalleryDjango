from django.shortcuts import render
from django.views.generic import list, detail
from Item.models import Item, Photo

class IndexListView(list.ListView):
    queryset = Item.objects.all()
    print(queryset)
#    print(queryset[0].get_absolute_url())
    template_name = "index.html"

class ItemListView(IndexListView):
    template_name = "items_list.html"

class ItemDetailView(detail.DetailView):
    queryset = Item.objects.all()
    template_name = "items_detail.html"

class PhotoDetailView(detail.DetailView):
    queryset = Photo.objects.all()
    template_name = "photos_detail.html"
