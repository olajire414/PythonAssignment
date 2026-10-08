import unittest

from dicttionary_application.bright_future import *


class BrightFutureTest(unittest.TestCase):
    def test_that_a_new_student_can_be_created(self):
        age = 21
        name = 'ola'
        courses = set()
        address= {}

        student_id = {
            'name' : name,
            'age' : age,
            'courses' :courses,
            'address' : address}

        self.assertEqual(student_id,create_new_student(name,age,courses,address))

    def test_that_a_student_whole_course_can_be_retrieved(self):
        age = 21
        name = 'ola'
        courses = {'physics', 'chemistry'}
        address = {}
        student_id = {'name': name,'age': age,'courses': courses,'address': address}
        self.assertEqual(courses,display_courses_of_a_single_student(student_id))

    def test_that_only_the_zip_code_can_be_returned(self):
            age = 21
            name = 'ola'
            courses = set ()
            address = {'city': 'lagos', 'zip_code': '12345'}
            student_id = {'name': name, 'age': age, 'courses': courses, 'address': address}
            self.assertEqual('12345',display_zipcode_of_an_address(student_id))

    def test_that_display_only_the_student_city(self):
        age = 21
        name = 'ola'
        courses = set ()
        address = {'city': 'lagos', 'zip_code': '12345'}
        student_id = {'name': name, 'age': age, 'courses': courses, 'address': address}
        self.assertEqual('lagos',display_student_city_of_an_address(student_id))

    def test_that_allows_a_student_to_add_a_new_course_not_in_his_course_and_official(self):
        new_course = 'Math'
        age = 21
        name = 'ola'
        courses = {'physics', 'chemistry'}
        address = {'city': 'lagos', 'zip_code': '12345'}
        student_id = {'name': name, 'age': age, 'courses': courses, 'address': address}
        self.assertEqual('Math',add_a_new_course(student_id,new_course))

    def test_that_update_student_course(self):
        age = 21
        name = 'ola'
        courses = {'physics', 'chemistry'}
        address = {'city': 'lagos', 'zip_code': '12345'}
        student_id = {'name': name, 'age': age, 'courses': courses, 'address': address}
        removed_course = student_id['courses'].remove('physics')
        self.assertEqual(removed_course,update_student_course(student_id,removed_course))

    def test_that_various_fields_can_be_updated(self):
        age = 21
        name = 'ola'
        courses = {'physics', 'chemistry'}
        address = {'city': 'lagos', 'zip_code': '12345'}
        student_id = {'name': name, 'age': age, 'courses': courses, 'address': address}
        expected =(name,age,address['city'],address['zip_code'])
        self.assertEqual(expected,update_student_fields(student_id,name,age,address['city'],address['zip_code']))

    def test_that_overall_number_of_student_can_be_displayed(self):
        students = {}
        age = 21
        name = 'ola'
        courses = {'physics', 'chemistry'}
        address = {'city': 'lagos', 'zip_code': '12345'}
        student1 = {'name': name, 'age': age, 'courses': courses, 'address': address}
        student2 = {'name': name, 'age': age, 'courses': courses, 'address': address}
        students.update({'id_001':student1})
        students.update({'id_002':student2})
        expected = len(students)

        self.assertEqual(expected,display_overall_numbers_of_student(students))

















    if __name__ == '__main__':
        unittest.main()
