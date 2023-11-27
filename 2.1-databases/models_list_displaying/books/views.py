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


def book_view_detail(request, pub_date: datetime):
    template = 'product.html'
    book = Book.objects.filter(pub_date=pub_date)
    previous_page = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    next_page = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    context = {'book': book, 'previous_page': previous_page, 'next_page': next_page}
    return render(request, template, context)
