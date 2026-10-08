official_courses = {"Math", "Physics", "Computer Science", "Biology", "Chemistry",
                    "Statistics", "English", "Economics", "History", "Philosophy",
                    "Sociology", "Political Science", "Geography", "Psychology",
                    "Art","Music", "Engineering", "Law", "Medicine", "Business"}

students = {}

def create_new_student(name,age,courses:set,address:dict)-> dict :

    student_id = {
        'name' : name,
        'age' : age,
        'courses' : courses,
        'address' : address
    }
    return student_id

def display_courses_of_a_single_student(student_id:dict):
    if(student_id['courses'] != None):
        return student_id['courses']
    return None


def display_zipcode_of_an_address(student_id:dict):
    if(student_id.get('address')!=None):
        return student_id['address'].get('zip_code')
    return None


def display_student_city_of_an_address(student_id:dict)->dict:
    if student_id != None:
        return student_id['address'].get('city')

def add_a_new_course(student_id:dict, new_course):

    if(student_id != None  and new_course in official_courses and new_course not in student_id['courses']):
        student_id['courses'].add(new_course)
        return new_course

def update_student_course(student_id:dict, course:set):
    if(student_id != None and course != None):
        student_id['courses'].remove(course)
        return course


def update_student_fields(student_id:dict,name,age,city,zipcode):
    if(student_id != None):

        student_id['name'] = name
        student_id['age'] = age
        student_id['address']['city'] = city
        student_id['address']['zipcode'] = zipcode
    return (student_id['name'],student_id['age'],student_id['address']['city'],student_id['address']['zipcode'])


def display_overall_numbers_of_student(students:dict)-> int:

        return len(students)







































