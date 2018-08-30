from mongoengine import *
from models.classes import *
from datetime import datetime
from faker import Faker as fake
import mlab

mlab.connect()

# new_admin = User(
#     name = "admin",
#     email = "thelivingdeath.n2h.destroyer@gmail.com",
#     phone_number = "123456789",
#     sign_in = "admin",
#     password = "admin",    
#     is_activating = True,
#     is_admin = True
# )
# new_admin.save()

   name = StringField(required=True)
    level = StringField()
    fee = IntField(required=True)
    content = StringField()
    detail = ListField()
    duration = DateTimeField()
    schedule_time = DateTimeField()
    is_activating = BooleanField(default=True)

new_course = Course(
    name = "Học guitar",
    level = "Basic",
    fee = 600000,
    content = "học guitar cơ bản",
    detail =  [
        {
            "Bài 1": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 1.",
            "link": "https://www.youtube.com/watch?v=bUaFlTUkL8E" 
        },
        {
        "Bài 2": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 2.",
        "link": "https://www.youtube.com/watch?v=MntHf8bdL4s"
        }   
    ],
    schedule_time = 2018,
    is_activating = True
)
new_course.save()
