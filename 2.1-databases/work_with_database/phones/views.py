from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == "name":
        phone_objects = Phone.objects.all().order_by('name').values()
    elif sort == "min_price":
        phone_objects = Phone.objects.all().order_by('price').values()
    else:
        phone_objects = Phone.objects.all().order_by('-price').values()
    context = {'phones': phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    print(slug)
    phone_object = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone_object}
    return render(request, template, context)
