from backend import db, Task, TestCase


def test_create_table():
    db.create_all()


def test_drop_table():
    db.drop_all()
