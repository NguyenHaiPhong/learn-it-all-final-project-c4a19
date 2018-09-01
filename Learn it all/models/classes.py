from mongoengine import *
from datetime import datetime

class User(Document):
    name = StringField()
    email = StringField(required=True)
    phone_number = StringField()
    sign_in = StringField(required=True, unique=True)
    password = StringField(required=True)
    is_activating = BooleanField(default=False)
    is_admin = BooleanField(default=False)

class Category(Document):
    name = StringField()

class Course(Document):
    name = StringField(required=True)
    level = StringField()
    fee = IntField(required=True)
    detail = ListField()
    duration = StringField()
    schedule_time = StringField()
    is_activating = BooleanField(default=True)
    category_id = ReferenceField(Category)

class Lecturer(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    height = IntField()
    weight = IntField()
    body_fat = IntField()
    phone_number = StringField()
    description = ListField()
    category_id = ReferenceField(Category)
    course_id = ReferenceField(Course)

class Order(Document):
    customer_id = ReferenceField(User)
    course_id = ReferenceField(Course)
    order_time = DateTimeField(default=datetime.now())
    is_purchased = BooleanField(default=False)

