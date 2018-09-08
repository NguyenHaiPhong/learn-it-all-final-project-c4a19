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

new_lecturer = Lecturer(
    name = "Nguyễn Hải Phong",
    description = ["Giảng viên Cao Đẳng Nghệ thuật Hà Nội"],
    category_id = "5b90986dfd2b0f3ed008a25c",
    course_id = ["5b93836bfd2b0f0460b11778","5b9389a6fd2b0f22ac4dd0cf"]
)
new_lecturer.save() 

new_lecturer_1 = Lecturer(
    name = "Nguyễn Thành Nam",
    description = ["Vô địch ESL One Hamburg 2017", "Á quân DreamLeague Mùa 8", "Vô địch TI 69", "Admin trang Dota 2 Fap Group"],
    category_id = "5b90986efd2b0f3ed008a25e",
    course_id = ["5b93836afd2b0f0460b11774","5b93836afd2b0f0460b11775","5b9389a6fd2b0f22ac4dd0d1"]
)
new_lecturer_1.save()

new_lecturer_2 = Lecturer(
    name = "Nguyễn Nhung",
    description = ["Vô địch Thế giới"],
    category_id = "5b90986efd2b0f3ed008a25e",
    course_id = ["5b9389a6fd2b0f22ac4dd0d0","5b93836afd2b0f0460b11776","5b93836bfd2b0f0460b11777"]
)
new_lecturer_2.save()


# new_course = Course(
#     name = "Guitar",
#     level = "Basic",
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
#     name = "League of Legends",
#     level = "Basic",
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
#     name = "Dota 2",
#     level = "Basic",
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
#     name = "Basketball",
#     level = "Basic",
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
#     name = "Football",
#     level = "Basic",
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

# new_course_5 = Course(
#     name = "PES",
#     level = "Basic",
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

# new_course = Course(
#     name = "Dota 2",
#     level = "Advance",
#     fee = 500000,
#     description = "Học chơi Dota 2 nâng cao",
#     detail = [
#         {
#             "Bài 1": "How to Harass & DOMINATE Your Midlane!",
#             "link": "https://www.youtube.com/watch?v=6IU7v9IRXIM"
#         },
#         {
#             "Bài 2": "Dota 2 - Advanced Carry Tips and Decision Making Tutorial",
#             "link": "https://www.youtube.com/watch?v=N8c9AyzOplo"
#         },
#         {
#             "Bài 3": "Ten Advanced DotA 2 Tips/Tricks/Mechanics with eSportsMonies",
#             "link": "https://www.youtube.com/watch?v=XbA-AKWPgBg"
#         },
#         {
#             "Bài 4": "Dota 2 Tips and Tricks advanced and for beginners 2018!",
#             "link": "https://www.youtube.com/watch?v=S0Dz9GV28tA"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25e"
# )
# new_course.save()

# new_course_1 = Course(
#     name = "Dota 2",
#     level = "Expert",
#     fee = 800000,
#     description = "Trở thành game thủ Dota 2 chuyên nghiệp",
#     detail = [
#         {
#             "Bài 1": "How to WIN IMPOSSIBLE Offlanes: Top Tips | Dota 2 Guide",
#             "link": "https://www.youtube.com/watch?v=szLsAFiNkFA"
#         },
#         {
#             "Bài 2": "Drafting the BEST Offlaner! | Dota 2 Guide",
#             "link": "https://www.youtube.com/watch?v=WpC1PHkiGbY"
#         },
#         {
#             "Bài 3": "Learn Dota 2 - Warding",
#             "link": "https://www.youtube.com/watch?v=VQn8UCNRc_U"
#         },
#         {
#             "Bài 4": "Dota2: Expert Gameplay Domination",
#             "link": "https://www.youtube.com/watch?v=Ku5V-7pZ2s4"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25e"
# )
# new_course_1.save()

# new_course_2 = Course(
#     name = "League of Legends",
#     level = "Advance",
#     fee = 430000,
#     description = "League of Legends nâng cao",
#     detail = [
#         {
#             "Bài 1": "Advanced Techniques",
#             "link": "https://www.youtube.com/watch?v=34n2HlpYIJo"
#         },
#         {
#             "Bài 2": "Trading and Harassing Advance Concepts - League of Legends Academia - Guide/Tutorial",
#             "link": "https://www.youtube.com/watch?v=grusUReGWEk"
#         },
#         {
#             "Bài 3": "League of Legends Advanced Tutorials - General Lane Setup",
#             "link": "https://www.youtube.com/watch?v=E_5InHiMj8s"
#         },
#         {
#             "Bài 4": "9 TIPS ON HOW TO WIN YOUR LANE IN LEAGUE OF LEGENDS",
#             "link": "https://www.youtube.com/watch?v=1L2f7rprnfo"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25e"
# )
# new_course_2.save()

# new_course_3 = Course(
#     name = "League of Legends",
#     level = "Expert",
#     fee = 1500000,
#     description = "Trở thành 1 game thủ Liên Minh chuyên nghiệp",
#     detail = [
#         {
#             "Bài 1": "League of Legends Macro Play 1: The Grid",
#             "link": "https://www.youtube.com/watch?v=EvbaqRYBXEo"
#         },
#         {
#             "Bài 2": "League of Legends Macro Play 2: Early Game Jungling Part 1",
#             "link": "https://www.youtube.com/watch?v=HGZtC2sGNFE"
#         },
#         {
#             "Bài 3": "League of Legends Macro Play 3: Early Game Jungling Part 2",
#             "link": "https://www.youtube.com/watch?v=ByqV0pPXoNU"
#         },
#         {
#             "Bài 4": "League of Legends Macro Play 4: Transitioning from Early to Mid Game",
#             "link": "https://www.youtube.com/watch?v=QdSQBD9aEhw"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25e"
# )
# new_course_3.save()

# new_course_4 = Course(
#     name = "Guitar",
#     level = "Expert",
#     fee = 1000000,
#     description = "Thành thục các kỹ thuật đánh Guitar",
#     detail = [
#         {
#             "Bài 1": "Modal Progressions For Guitar - Guitar Lesson",
#             "link": "https://www.youtube.com/watch?v=TZbqqB8lQX0"
#         },
#         {
#             "Bài 2": "Understanding Modal Chord Progressions",
#             "link": "https://www.youtube.com/watch?v=5r4tDMqzOYA"
#         },
#         {
#             "Bài 3": "How To Write Chord Progressions - Songwriting Basics [Music Theory - Diatonic Chords]",
#             "link": "https://www.youtube.com/watch?v=M8eItITv8QA"
#         },
#         {
#             "Bài 4": "Deconstructing Diminished Chords - Music Theory for Guitar",
#             "link": "https://www.youtube.com/watch?v=HQ2pg7D1aks"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986dfd2b0f3ed008a25c"
# )
# new_course_4.save()

# new_course_5 = Course(
#     name = "Gym",
#     level = "Advance",
#     fee = 790000,
#     description = "Các kỹ thuật nâng cao về Gym",
#     detail = [
#         {
#             "Bài 1": "TOP 5 Gym Tips",
#             "link": "https://www.youtube.com/watch?v=vPKcShZzuPo"
#         },
#         {
#             "Bài 2": "The PROPER Way To Lift Weights (Stop Doing This!)",
#             "link": "https://www.youtube.com/watch?v=I3zfre75XW0"
#         },
#         {
#             "Bài 3": "7 MUST KNOW Gym Hacks & Tips",
#             "link": "https://www.youtube.com/watch?v=0fvsTADOA5Y"
#         },
#         {
#             "Bài 4": "3 Common Beginner Workout Mistakes",
#             "link": "https://www.youtube.com/watch?v=79vqkTk2QzE"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25d"
# )
# new_course_5.save()

# new_course_6 = Course(
#     name = "Gym",
#     level = "Expert",
#     fee = 430000,
#     description = "Thành thạo những kĩ thuật trong thể hình",
#     detail = [
#         {
#             "Bài 1": "6 Muscle Gaining Mistakes (SLOW OR NO GROWTH!!)",
#             "link": "https://www.youtube.com/watch?v=330Ufcaj1zA"
#         },
#         {
#             "Bài 2": "The Official Bench Press Check List (AVOID MISTAKES!)",
#             "link": "https://www.youtube.com/watch?v=vthMCtgVtFw"
#         },
#         {
#             "Bài 3": "3 Sets of 12 is KILLING Your Gains!!",
#             "link": "https://www.youtube.com/watch?v=vKDYfRtfqng"
#         },
#         {
#             "Bài 4": "Chest Workout Tips for Size (HARDGAINER EDITION!)",
#             "link": "https://www.youtube.com/watch?v=nmsFJHkWkfo"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25d"
# )
# new_course_6.save()

# new_course_7 = Course(
#     name = "Football",
#     level = "Advance",
#     fee = 420000,
#     description = "Các kỹ thuật nâng cao trong bóng đá",
#     detail = [
#         {
#             "Bài 1": "Improve Your Football Fitness - Pre Season Training Camp",
#             "link": "https://www.youtube.com/watch?v=SkfdOThWeZA"
#         },
#         {
#             "Bài 2": "How to run longer | How to increase stamina and endurance | How to run properly | Soccer Football",
#             "link": "https://www.youtube.com/watch?v=uE15A4qom20"
#         },
#         {
#             "Bài 3": "Strength Training For Football | Full-Body Gym Workout | You Ask, We Answer",
#             "link": "https://www.youtube.com/watch?v=Pyd8vSu0AOw"
#         },
#         {
#             "Bài 4": "England Get to Work in the Gym Ahead of Tunisia | Inside Training | World Cup 2018",
#             "link": "https://www.youtube.com/watch?v=6bFHDttjtEc"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25d"
# )
# new_course_7.save()

# new_course_8 = Course(
#     name = "Football",
#     level = "Expert",
#     fee = 900000,
#     description = "Thành thạo các kỹ năng trong bóng đá",
#     detail = [
#         {
#             "Bài 1": "Individual Football Training",
#             "link": "https://www.youtube.com/watch?v=IR0Y2DRWJrQ"
#         },
#         {
#             "Bài 2": "How To Warm Up Before A Soccer / Football Game",
#             "link": "https://www.youtube.com/watch?v=ij57OFjvwpk"
#         },
#         {
#             "Bài 3": "100 Individual Soccer Training Drills",
#             "link": "https://www.youtube.com/watch?v=z7jP3moQi9c"
#         },
#         {
#             "Bài 4": "How to train on your own | 3 individual football training drills",
#             "link": "https://www.youtube.com/watch?v=Y8i6QDPQ0v0"
#         }
#     ],
#     schedule_time = "2018",
#     is_activating = True,
#     category_id = "5b90986efd2b0f3ed008a25d"
# )
# new_course_8.save()

