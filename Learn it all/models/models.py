from mongoengine import *
from datetime import datetime

class User(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    phone_number = StringField()
    sign_in = StringField(required=True, unique=True)
    password = StringField(required=True)
    is_activating = BooleanField(default=False)
    is_admin = BooleanField(default=False)

class Course(Document):
    name = StringField(required=True)
    fee = IntField(required=True)
    content = StringField()
    time = DateTimeField()
    is_activating = BooleanField(default=True)

class Lecturer(Document):
    name = StringField(required=True)
    email = StringField(required=True)
    height = IntField()
    weight = IntField()
    body_fat = IntField()
    phone_number = StringField()
    description = ListField()
    specialized = StringField()

class Order(Document):
    customer_id = ReferenceField(User)
    course_id = ReferenceField(Course)
    order_time = DateTimeField(default=datetime.now())
    is_purchased = BooleanField(default=False)

