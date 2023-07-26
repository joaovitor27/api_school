from django.test import TestCase
from school.models import Course


class CourseModelTestCase(TestCase):
    def setUp(self):
        self.course = Course.create(
            name='Python',
            description='Python',
            level='B',
            price=1000.00
        )

    def test_course_create(self):
        self.assertTrue(isinstance(self.course, Course))
        self.assertEqual(self.course.__str__(), self.course.name)

    def test_fields_course(self):
        self.assertTrue(hasattr(self.course, 'name'))
        self.assertTrue(hasattr(self.course, 'description'))
        self.assertTrue(hasattr(self.course, 'level'))
        self.assertTrue(hasattr(self.course, 'price'))
        self.assertTrue(hasattr(self.course, 'code'))

    def test_value_fields_course(self):
        self.assertEqual(self.course.name, 'Python' or self.course.code)
        self.assertEqual(self.course.description, 'Python')
        self.assertEqual(self.course.level, 'B')
        self.assertEqual(self.course.price, 1000.00)
        self.assertEqual(len(self.course.code), 8)
