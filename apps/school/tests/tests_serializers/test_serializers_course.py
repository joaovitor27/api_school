from django.test import TestCase
from school.models import Course
from school.serializer import CourseSerializer


class CourseSerializerTestCase(TestCase):
    def setUp(self) -> None:
        self.course = Course.create(
            name='Python',
            description='Python',
            level='B',
            price=1000.00
        )
        self.course_serializer = CourseSerializer(instance=self.course)

    def test_verify_fields_serializers(self):
        data = self.course_serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'description', 'level', 'price'})

    def test_verify_content_fields_serializers(self):
        data = self.course_serializer.data
        self.assertEqual(data['name'], self.course.name)
        self.assertEqual(data['description'], self.course.description)
        self.assertEqual(data['level'], self.course.level)
        self.assertEqual(float(data['price']), self.course.price)

    def test_verify_type_fields_serializers(self):
        data = self.course_serializer.data
        self.assertIsInstance(data['id'], int)
        self.assertIsInstance(data['name'], str)
        self.assertIsInstance(data['description'], str)
        self.assertIsInstance(data['level'], str)
        self.assertIsInstance(data['price'], str)
