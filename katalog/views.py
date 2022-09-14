from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog' : data_barang_katalog,
        'nama' : 'Sakinah Richas',
        'studentid' : '2106751511'
    }
    return render (request, "katalog.html", context)
