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

# new_category = Category(
#     name = "Âm Nhạc"
# )
# new_category.save()

# new_category_1 = Category(
#     name = "Thể Thao"
# )
# new_category_1.save()

# new_category_2 = Category(
#     name = "Thể Thao Điện Tử"
# )
# new_category_2.save()

    # new_course = Course(
    # name = "Học guitar",
    # level = "Basic",
    # fee = 600000,
    # content = "học guitar cơ bản",
    # detail =  [
    #     {
    #         "Bài 1": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 1.",
    #         "link": "https://www.youtube.com/watch?v=EDhzQNqo2T0&index=1&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr" 
    #     },
    #     {
    #         "Bài 2": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 2.",
    #         "link": "https://www.youtube.com/watch?v=zGVQ84h1JfI&index=2&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr"
    #     },

    #     {
    #         "Bài 3": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 3",
    #         "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=3"
    #     },
    #     {
    #         "Bài 4": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 4",
    #         "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=4"
    #     },
    #     {
    #         "Bài 5": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 5",
    #         "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=5"
    #     },
    #     {
    #         "Bài 6": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 6",
    #         "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=6"
    #     }
    # ],
    # schedule_time = 2018,
    # is_activating = True
    # )
    # new_course.save()

# new_lecturer = Lecturer(
#     name = "Nguyễn Hải Phong",
#     description = ["Giảng viên Cao Đẳng Nghệ thuật Hà Nội"],
#     category_id = "5b90986dfd2b0f3ed008a25c",
#     course_id = "5b90cfedfd2b0f30545288ee"
# )
# new_lecturer.save() 

# new_lecturer_1 = Lecturer(
#     name = "Nguyễn Thành Nam",
#     description = ["Vô địch ESL One Hamburg 2017", "Á quân DreamLeague Mùa 8", "Vô địch TI 69", "Admin trang Dota 2 Fap Group"],
#     category_id = "5b90986efd2b0f3ed008a25e",
#     course_id = "5b90cfedfd2b0f30545288f0"
# )
# new_lecturer_1.save()

# new_lecturer_2 = Lecturer(
#     name = "Nguyễn Nhung",
#     description = ["Vô địch Thế giới"],
#     category_id = "5b90986efd2b0f3ed008a25e",
#     course_id = "5b90cfedfd2b0f30545288ef"
# )
# new_lecturer_2.save()


# new_course = Course(
#     name = "Học guitar cơ bản",
#     level = "Cơ bản",
#     fee = 600000,
#     description = "Học guitar cơ bản",
#     detail = [
#         {
#             "Bài 1": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 1.",
#             "link": "https://www.youtube.com/watch?v=EDhzQNqo2T0&index=1&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr"
#         },
#         {
#             "Bài 2": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 2.",
#             "link": "https://www.youtube.com/watch?v=zGVQ84h1JfI&index=2&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr"
#         },
#         {
#             "Bài 3": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 3",
#             "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=3"
#         },
#         {
#             "Bài 4": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 4",
#             "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=4"
#         },
#         {
#             "Bài 5": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 5",
#             "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=5"
#         },
#         {
#             "Bài 6": "Hướng dẫn tập guitar (cho người mới bắt đầu)_BÀI 6",
#             "link": "https://www.youtube.com/watch?v=x1k-Kepemgk&list=PL-RYb_OMw7Gf5Y6HfdXrn5s4Y5oXb2zkr&index=6"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986dfd2b0f3ed008a25c"   
# )
# new_course.save()

# new_course_1 = Course(
#     name = "Liên Minh Huyền Thoại nhập môn",
#     level = "Cơ bản",
#     fee = 200000,
#     description = "Học chơi Liên Minh Huyền Thoại cơ bản",
#     detail = [
#         {
#             "Bài 1": "Ôn lại kỹ năng cơ bản"
#         },
#         {
#             "Bài 2": "Kỹ năng đầu tiên",
#             "Link": "https://www.youtube.com/watch?v=F30c8La12Rg"
#         },
#         {
#             "Bài 3": "Trận đấu đầu tiên",
#             "Link": "https://www.youtube.com/watch?v=2IMnqEga6tc"
#         }
#     ],
#     schedule_time =  "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25e"
# )
# new_course_1.save()

# new_course_2 = Course(
#     name = "Dota 2 nhập môn",
#     level = "Cơ bản",
#     fee = 322000,
#     description = "Học chơi Dota 2 cơ bản",
#     detail = [
#         {
#             "Bài 1": "Ôn lại kiến thức của bạn"
#         },
#         {
#             "Bài 2": "Đây là Dota 2",
#             "Link": "https://www.youtube.com/watch?v=9Szj-CloJiI"
#         },
#         {
#             "Bài 3": "Làm quen với map",
#             "Link": "https://www.youtube.com/watch?v=KWPWDWyzFso"
#         },
#         {
#             "Bài 4": "Điều khiển các tướng",
#             "Link": "https://www.youtube.com/watch?v=3KbAMEnsRLg"
#         },
#         {
#             "Bài 5": "Đồ cần thiết cho 1 trận chiến",
#             "Link": "https://www.youtube.com/watch?v=7KQ_ysnhpnI"
#         },
#         {
#             "Bài 6": "Các dấu hiệu trong trận chiến",
#             "Link": "https://www.youtube.com/watch?v=EKHk6Ba_dwA&list=PLwL7E8fRVEdc0tFJlm2AWYhu4ccMk_vDD&t=0s&index=10"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25e"
# )
# new_course_2.save()

# new_course_3 = Course(
#     name = "Học bóng rổ cơ bản",
#     level = "Cơ bản",
#     fee = 200000,
#     description = "Học chơi bóng rổ cơ bản",
#     detail = [
#         {
#             "Bài 1": "Kỹ thuật ném bóng cơ bản",
#             "Link": "https://www.youtube.com/watch?v=nqqw_hYT4QM&list=PLpBIZ-08VrsVimGt72BC2F-lejx3FM1pI"
#         },
#         {
#             "Bài 2": "Kỹ thuật ném bóng khi di chuyển",
#             "Link": "https://www.youtube.com/watch?v=NU7yES0O94Y&list=PLpBIZ-08VrsVimGt72BC2F-lejx3FM1pI&index=2"
#         },
#         {
#             "Bài 3": "Kỹ thuật ném bóng khi rê bóng",
#             "Link": "https://www.youtube.com/watch?v=j128B5vOdSM&index=3&list=PLpBIZ-08VrsVimGt72BC2F-lejx3FM1pI"
#         },
#         {
#             "Bài 4": "Kỹ thuật phòng thủ",
#             "Link": "https://www.youtube.com/watch?v=pXy7eZjD88I&index=4&list=PLpBIZ-08VrsVimGt72BC2F-lejx3FM1pI"
#         },
#         {
#             "Bài 5": "Kỹ năng rê bóng và kiểm soát bóng",
#             "Link": "https://www.youtube.com/watch?v=lYDLJevy5MQ&index=4&list=PLpBIZ-08VrsUgcMHifXoJcnGGe82D5ccU"
#         },
#         {
#             "Bài 6": "Kỹ năng kiểm soát bóng khi di chuyển",
#             "Link": "https://www.youtube.com/watch?v=3UOJEPWHjR0&index=6&list=PLpBIZ-08VrsUgcMHifXoJcnGGe82D5ccU"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25d"
# )
# new_course_3.save()

# new_course_4 = Course(
#     name = "Học bóng đá cơ bản",
#     level = "Cơ bản",
#     fee = 200000,
#     description = "Học chơi bóng đá cơ bản",
#     detail = [
#         {
#             "Bài 1": "Rê bóng",
#             "Link": "https://www.youtube.com/watch?v=lCQ4gLVBLzg&list=PLqvvsIDxQFrmsAsnE5ezgk6B4tYl1VJzH"
#         },
#         {
#             "Bài 2": "Kỹ thuật chuyền bóng",
#             "Link": "https://www.youtube.com/watch?v=0lhZeur2g_8"
#         },
#         {
#             "Bài 3": "Kỹ thuật sút bóng",
#             "Link": "https://www.youtube.com/watch?v=XSOx4wMnNbA"
#         }
#     ],
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25d"
# )
# new_course_4.save()

# {
#     "_id": {
#         "$oid": "5b8fe7acdb57d20184b77325"
#     },
#     "name": "Gym",
#     "level": "Basic",
#     "fee": 200000,
#     "detail": [
#         {
#             "Bài 1": "https://www.youtube.com/watch?v=IGhQtwzfmXM&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p"
#         },
#         {
#             "Bài 2": "https://www.youtube.com/watch?v=90AABclAL1M&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p&index=2"
#         },
#         {
#             "Bài 3": "https://www.youtube.com/watch?v=IbrGAh_FdAw&index=3&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p"
#         },
#         {
#             "Bài 4": "https://www.youtube.com/watch?v=RCIys_TFTYo&index=4&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p"
#         },
#         {
#             "Bài 5": "https://www.youtube.com/watch?v=RCIys_TFTYo&index=4&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p"
#         },
#         {
#             "Bài 6": "https://www.youtube.com/watch?v=lqBjWkpMii0&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p&index=5"
#         },
#         {
#             "Bài 7": "https://www.youtube.com/watch?v=lqBjWkpMii0&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p&index=5"
#         },
#         {
#             "Bài 8": "https://www.youtube.com/watch?v=Pcnsx5hI8ys&list=PLTs18vRP6TzfL2roQZUeWi0dteh8AEX-p&index=6"
#         }
#     ],
#     "is_activating": true,
#     "category_id": {
#         "$oid": "5b8f8cf8db57d203b8564782"
#     }
# }

# new_course_5 = Course(
#     name = "Pes nhập môn",
#     level = "Cơ bản",
#     fee = 200000,
#     description = "Học chơi PES cơ bản",
#     detail = [
#         {
#             "Bai 1": "Huong dan ky nang da pes don gian"
#         },
#         {
#             "Bai 2": "Kỹ năng lốp bóng",
#             "Link": "https://www.youtube.com/watch?v=WKXvfjNf0M4&list=PLa4NwL0WA6cb8dlSxuaaJjVd9Z3wH9ZkJ"
#         },
#         {
#             "Bài 3": "Chiến thuật phòng thủ",
#             "Link": "https://www.youtube.com/watch?v=BuMX1sJHMTw&t=176s"
#         },
#         {
#             "Bài 4": "Chiến thuật phòng ngự tấn công",
#             "Link": "https://www.youtube.com/watch?v=PNVYOzpgCoA"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25e"
# )
# new_course_5.save()

# {
#     "_id": {
#         "$oid": "5b8fe7addb57d20184b77326"
#     },
#     "name": "Guitar Advance",
#     "level": "Advance",
#     "fee": 400000,
#     "detail": [
#         {
#             "Bài 1": "",
#             "Link": "https://www.youtube.com/watch?v=lut3mV5zkaM&list=PLB0A8BDDB9DBF223A&index=2"
#         },
#         {
#             "Bài 2": "",
#             "Link": "https://www.youtube.com/watch?v=ZA5cVPZlkaA&index=3&list=PLB0A8BDDB9DBF223A"
#         },
#         {
#             "Bài 3": "",
#             "Link": "https://www.youtube.com/watch?v=7meLvrquplQ&index=4&list=PLB0A8BDDB9DBF223A"
#         },
#         {
#             "Bài 4": "",
#             "Link": "https://www.youtube.com/watch?v=o5FbP7HLkTI&list=PLB0A8BDDB9DBF223A&index=5"
#         },
#         {
#             "Bài 5": "",
#             "Link": "https://www.youtube.com/watch?v=iNU9KVq5ReY&list=PLB0A8BDDB9DBF223A&index=6"
#         },
#         {
#             "Bài 6": "",
#             "Link": "https://www.youtube.com/watch?v=ehCEoc5PVGM&list=PLB0A8BDDB9DBF223A&index=7"
#         },
#         {
#             "Bài 7": "",
#             "Link": "https://www.youtube.com/watch?v=1RXP6EkZim4&list=PLB0A8BDDB9DBF223A&index=8"
#         }
#     ],
#     "is_activating": true,
#     "category_id": {
#         "$oid": "5b8f8cf8db57d203b8564782"
#     }
# }


