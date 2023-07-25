import random

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from school.models import Course


class CourseTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse('v1:course-list')
        self.courses = ['Python', 'Django', 'Java']
        self.course_1 = Course.objects.create(
            code='{}{}-{}'.format(self.courses[0].upper(), random.randrange(100, 999), random.randrange(1, 9)),
            name=self.courses[0],
            description=self.courses[0],
            level='B',
            price=1000.00
        )
        self.course_2 = Course.objects.create(
            code='{}{}-{}'.format(self.courses[1].upper(), random.randrange(100, 999), random.randrange(1, 9)),
            name=self.courses[1],
            description=self.courses[1],
            level='I',
            price=2000.00
        )
        self.course_3 = Course.objects.create(
            code='{}{}-{}'.format(self.courses[2].upper(), random.randrange(100, 999), random.randrange(1, 9)),
            name=self.courses[2],
            description=self.courses[2],
            level='A',
            price=3000.00
        )

    def test_get_list_courses(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)

    def test_get_courses(self):
        response = self.client.get('/api/v1/course/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.courses[0])

    def test_post_course(self):
        data = {
            "name": "course Teste 4",
            "description": "course Teste 4",
            "level": "B",
            "price": 1000.00
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 4)
        self.assertEqual(Course.objects.get(pk=4).name, data['name'])

    def test_put_course(self):
        data = {
            "name": "course Teste 5",
            "description": "course Teste 5",
            "level": "A",
            "price": 5000.00
        }
        response = self.client.put('/api/v1/course/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.count(), 3)
        self.assertEqual(Course.objects.get(pk=1).name, data['name'])
        print(response.data)

    def test_delete_course(self):
        response = self.client.delete('/api/v1/course/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
