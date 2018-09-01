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

# new_course = Course(
#     name = "Học guitar",
#     level = "Basic",
#     fee = 600000,
#     detail = [
#         {
#             "Bài 1": "Guitar Basics",
#             "link": "https://www.youtube.com/watch?v=3vJw4S_9uWM"
#         },
#         {
#             "Bài 2": "How to Play Guitar Chords",
#             "link": "https://www.youtube.com/watch?v=jCG3YgSSqbQ"
#         },
#         {
#             "Bài 3": "How to Change Chords",
#             "link": "https://www.youtube.com/watch?v=q9ThDTiuyFE"
#         }
#     ],
#     duration = "haha",
#     schedule_time = "haha",
#     is_activating = True,
#     category_id = "5b8949f3fd2b0f1d48f368e3",
# )
# new_course.save()

# new_category = Category(
#     name = "Music"
# )
# new_category.save()

new_lecturer = Lecturer(
    name = "Nguyễn Hải Phong",
    email = "phong@gmail.com",
    description = ["Sinh viên năm 2 Cao Đẳng Nghệ thuật Hà Nội"],
    category_id = "5b8949f3fd2b0f1d48f368e3",
    course_id = "5b894c7afd2b0f15009135f1"
)
new_lecturer.save()