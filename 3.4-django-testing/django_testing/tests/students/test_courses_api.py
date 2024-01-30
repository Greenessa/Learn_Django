import pytest
import json
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Student, Course

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory
@pytest.fixture
def student_factory():
    def factory2(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory2

@pytest.fixture
def client():
    return APIClient()


#проверка получения первого курса
@pytest.mark.django_db
def test_first_course(client, course_factory, student_factory):
    courses=course_factory(_quantity=1, make_m2m=True)
    students=student_factory(_quantity=3, make_m2m=True)
    response= client.get('/api/v1/courses/')
    data=response.json()
    assert response.status_code == 200
    for i, c in enumerate(data):
        assert c['name']==courses[i].name


#проверка получения списка курсов
@pytest.mark.django_db
def test_list_courses(client, course_factory, student_factory):
    #Arrange
    count = Course.objects.count()
    courses = course_factory(_quantity=5, make_m2m=True)
    students = student_factory(_quantity=10, make_m2m=True)
    response= client.get('/api/v1/courses/')
    data=response.json()
    assert response.status_code == 200
    for i, c in enumerate(data):
        assert c['name']==courses[i].name
    assert Course.objects.count() == count+5
    assert len(data) == len(courses)

#проверка фильтрации списка курсов по id
@pytest.mark.django_db
def test_filter_id_courses(client, course_factory, student_factory):
    courses = course_factory(_quantity=5, make_m2m=True)
    course_id=courses[0].id
    students = student_factory(_quantity=10, make_m2m=True)
    response = client.get('/api/v1/courses/', {'id': course_id})
    data = response.json()
    cour1=Course.objects.filter(id=course_id)
    assert response.status_code == 200
    assert data['name']==cour1['name']

#ТЕСТ УСПЕШНОГО СОЗДАНИЯ курса
@pytest.mark.django_db
def test_create_course(client, course_factory, student_factory):
    # courses=course_factory(_quantity=1)
    # students=student_factory(_quantity=3)
    with open('data.json', encoding="utf-8") as f:
        data=json.load(f)
    #course1=Course.objects.create(name=data['name'])
    course1=client.post('/api/v1/courses/', {'name': data['name']})
    for d in data['students']:
        course1.students.create(name=d['name'], birth_date=d['birth_date'])
    response= client.get('/api/v1/courses/')
    data1=response.json()
    assert response.status_code == 200
    assert data1[0]['name']==course1.name

#тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    courses=course_factory(_quantity=1)
    students=student_factory(_quantity=3)
    with open('data.json', encoding="utf-8") as f:
        data=json.load(f)
    course1 = Course.objects.filter(id=1).update(name=data['name'])
    for d in data['students']:
        course1.students.all().update(name=d['name'], birth_date=d['birth_date'])
    response = client.get('/api/v1/courses/')
    data1 = response.json()
    assert response.status_code == 200
    assert data1[0]['name'] == course1.name

#тест успешного удаления курса.
@pytest.mark.django_db
def test_remove_course(client):
    with open('data.json', encoding="utf-8") as f:
        data=json.load(f)
    course1=Course.objects.create(name=data['name'])
    for d in data['students']:
        course1.students.create(name=d['name'], birth_date=d['birth_date'])
    course1.students.clear()
    Student.objects.all().delete()
    Course.objects.all().delete()
    response = client.get('/api/v1/courses/')
    data1 = response.json()
    assert response.status_code == 200
    assert len(data1)==0