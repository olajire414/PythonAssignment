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

def add_a_new_course(student_id:dict, new_courses):
    if(student_id != None):
        return student_id['courses'].add(new_courses)






































