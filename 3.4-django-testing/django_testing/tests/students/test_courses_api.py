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
    courses=course_factory(_quantity=3, make_m2m=True)
    course_id = courses[0].id
    students=student_factory(_quantity=5, make_m2m=True)
    response = client.get('/api/v1/courses/', {'id': course_id})
    data=response.json()
    assert response.status_code == 200
    assert data[0]['name']==courses[0].name


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

#проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_filter_name_courses(client, course_factory, student_factory):
    courses = course_factory(_quantity=5, make_m2m=True)
    course_name=courses[0].name
    students = student_factory(_quantity=10, make_m2m=True)
    response = client.get('/api/v1/courses/', {'name': course_name})
    data = response.json()
    cour1=Course.objects.filter(name=course_name)
    assert response.status_code == 200
    assert data['name']==cour1['name']

#ТЕСТ УСПЕШНОГО СОЗДАНИЯ курса
@pytest.mark.django_db
def test_create_course(client, course_factory, student_factory):
    with open('data.json', encoding="utf-8") as f:
        data=json.load(f)
    course1=client.post('/api/v1/courses/', {'name': data['name'], 'students': data['students']})
    response= client.get('/api/v1/courses/')
    data1=response.json()
    assert response.status_code == 200
    assert data1[0]['name']==course1.name

#тест успешного обновления курса
@pytest.mark.django_db
def test_update_course(client, course_factory, student_factory):
    courses = course_factory(_quantity=5, make_m2m=True)
    course_id = courses[0].id
    students = student_factory(_quantity=10, make_m2m=True)
    with open('data.json', encoding="utf-8") as f:
        data=json.load(f)
    course1 = client.patch('/api/v1/courses/', {'id': course_id, 'name': data['name'], 'students': data['students']})
    response = client.get('/api/v1/courses/', {'id': course_id})
    data1 = response.json()
    assert response.status_code == 200
    assert data1[0]['name'] == data['name']

#тест успешного удаления курса.
@pytest.mark.django_db
def test_remove_course(client, course_factory, student_factory):
    courses = course_factory(_quantity=2, make_m2m=True)
    course_id = courses[0].id
    students = student_factory(_quantity=5, make_m2m=True)
    course1 = client.delete('/api/v1/courses/', {'id': course_id})
    response = client.get('/api/v1/courses/')
    data1 = response.json()
    assert response.status_code == 200
    assert len(data1)==len(courses)-1

