from django.core.management.base import BaseCommand

from books.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        book1 = Book(name='Скотный двор', author='Джордж Оруэл', pub_date='2018-09-21')
        book1.save()
        book2 = Book(name='В память о прошлом земли', author='Лю Цысинь', pub_date='2018-09-21')
        book2.save()
        # TODO: Добавьте сохранение модели

