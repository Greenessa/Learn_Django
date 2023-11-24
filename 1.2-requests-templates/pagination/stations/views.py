import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        # получите текущую страницу и передайте ее в контекст
        # также передайте в контекст список станций на странице
        paginator = Paginator(reader, 10)
        page_number = int(request.GET.get('page', 1))
        page=paginator.get_page(page_number)
        context = {
            'bus_stations': page.object_list,
            'page': page,
        }
    return render(request, 'stations/index.html', context)


# contact_list = Women.objects.all()
# paginator = Paginator(contact_list, 3)
#
# page_number = request.GET.get('page')
# page_obj = paginator.get_page(page_number)
# list = []
# dict = {}
# with open(settings.BUS_STATION_CSV, newline='', encoding='utf-8') as csvfile:
#     reader = csv.DictReader(csvfile)
#     #print(reader)
#     for row in reader:
#         print(row)
#         dict['Name'] = row['Name']
#         dict['Street'] = row['Street']
#         dict['District'] = row['District']
        #print(dict)
        #list.append(dict)
        #print(list)