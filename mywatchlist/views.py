from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_mywatchlist(request):
    data_mywatchlist = MyWatchList.objects.all()
    
    sudahDitonton = MyWatchList.objects.filter(watched=True).count()
    belumDitonton = MyWatchList.objects.filter(watched=False).count()

    if sudahDitonton >= belumDitonton:
        pesan = "Selamat, kamu sudah banyak menonton!"
    else:
        pesan = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_mywatch' : data_mywatchlist,
        'pesan' : pesan,
        'nama' : 'Sakinah Richas',
        'studentid' : '2106751511'
    }
    return render (request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_html(request):
    data = MyWatchList.objects.all()
    context = {
        'list_mywatch' : data,
        
    }
    return render (request, "mywatchlistHTML.html", context)