
from pprint import pprint

from django.core.management.base import BaseCommand
from school.models import Student, Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        st1 = Student.objects.create(name="Иванов Иван", group="8A")
        st2 = Student.objects.create(name="Безгода Михаил", group="8A")
        st3 = Student.objects.create(name="Безлюдный Олег", group="8Б")
        teach1 = Teacher.objects.create(name="Корякин Василий Петрович", subject="Алгебра")
        teach2= Teacher.objects.create(name="Петров Василий Иванович", subject="Физика")
        teach3 = Teacher.objects.create(name="Васечкин Игорь Иванович", subject="История")
        teach1.students.add(st1)
        teach1.students.add(st2)
        teach1.students.add(st3)
        teach2.students.add(st1)
        teach2.students.add(st2)
        teach2.students.add(st3)
        teach3.students.add(st1)
        teach3.students.add(st2)
        # en1 = Student.objects.all()
        # en1.delete()
        # en2 = Teacher.objects.all()
        # en2.delete()