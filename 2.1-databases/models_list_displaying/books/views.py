from datetime import datetime

from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from books.models import Book


def books_view_index(request):
    return redirect('books')

def books_view(request):
    template = 'catalog.html'
    b = Book.objects.all()
    context = {'books': b}
    return render(request, template, context)

# def book_view(request):
#     template = ''
#     b = list(Book.objects.all())
#     paginator = Paginator(b, 1)
#     page_number = int(request.GET.get('page', 1))
#     page = paginator.get_page(page_number)
#     context = {
#         'book': page.object_list,
#         'page': page,
#     }
#     return render(request, 'stations/index.html', context)
def book_view(request, pub_date: datetime):
    template = 'product.html'
    #book = Book.objects.filter(pub_date__contains=pub_date).first()
    b = list(Book.objects.all())
    paginator = Paginator(b, 1)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {'book': page.object_list}
    return render(request, template, context)
