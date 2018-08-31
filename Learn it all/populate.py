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
            "link": "https://www.youtube.com/watch?v=EDhzQNqo2T0&index=1&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr" 
        },
        {
            "Bài 2": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 2.",
            "link": "https://www.youtube.com/watch?v=zGVQ84h1JfI&index=2&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr"
        },

        {
            "Bài 3": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 3",
            "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=3"
        },
        {
            "Bài 4": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 4",
            "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=4"
        },
        {
            "Bài 5": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 5",
            "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=5"
        },
        {
            "Bài 6": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 6",
            "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=6"
        }
    ],
    schedule_time = 2018,
    is_activating = True
    )
    new_course.save()
