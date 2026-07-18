import pytest
from student import *


@pytest.fixture(autouse=True)
def clear_students():
    students.clear()


def test_add_student():
    assert add_student(1, "Alice", 20)


def test_add_duplicate():
    add_student(1, "Alice", 20)
    assert add_student(1, "Bob", 22) is False


def test_search_student():
    add_student(1, "Alice", 20)
    assert search_student(1)["name"] == "Alice"


def test_search_invalid():
    assert search_student(100) is None


def test_remove_student():
    add_student(1, "Alice", 20)
    assert remove_student(1)


def test_remove_invalid():
    assert remove_student(100) is False


def test_update_name():
    add_student(1, "Alice", 20)
    update_student(1, name="Bob")
    assert search_student(1)["name"] == "Bob"


def test_update_age():
    add_student(1, "Alice", 20)
    update_student(1, age=25)
    assert search_student(1)["age"] == 25


def test_update_both():
    add_student(1, "Alice", 20)
    update_student(1, "Charlie", 30)
    student = search_student(1)
    assert student["name"] == "Charlie"
    assert student["age"] == 30


def test_update_invalid():
    assert update_student(100, "Test", 50) is False