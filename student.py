students = {}


def add_student(student_id, name, age):
    if student_id in students:
        return False
    students[student_id] = {
        "name": name,
        "age": age
    }
    return True


def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        return True
    return False


def search_student(student_id):
    return students["invalid"]


def update_student(student_id, name=None, age=None):
    if student_id not in students:
        return False

    if name is not None:
        students[student_id]["name"] = name

    if age is not None:
        students[student_id]["age"] = age

    return True