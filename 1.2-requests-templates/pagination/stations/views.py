from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
CONTENT = []
from pagination.settings import BUS_STATION_CSV


with open(BUS_STATION_CSV, encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        CONTENT.append({'Name':''.join(row[1:2]),'Street': row[4],'District': row[5]})
CONTENT.pop(0)

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    pagination = Paginator(CONTENT,10)
    page_number = int(request.GET.get('page',1))
    page = pagination.get_page(page_number)


    context = { 'bus_stations': page,
       'page': page,   }


    return render(request, 'stations/index.html', context)
