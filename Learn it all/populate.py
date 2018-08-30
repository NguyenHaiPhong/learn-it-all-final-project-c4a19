from models.models import *
import mlab
from pymongo import *
from random import choice
import datetime

mlab.connect()

# Course List
basic_course = Course(
    
    name = "Basic",
    fee = 20,
    content = ('Bạn sẽ được xem các video cơ bản từ các giảng viên chất lượng nhất hệ mặt trời',
    'Cung cấp cho bạn bộ giáo trình cơ bản về môn học mà bạn chọn', ''
    ),
    time = "3 Buổi",
    is_activating = False
)
basic_course.save()

intensive_course = Course(
    name = "Intensive",
    fee = 50,
    time = "7 Buổi",
    content = (['Bạn sẽ được tương tác với giảng viên cùng các học viên khác thông qua lớp học Online',
        'Cung cấp cho bạn bộ giáo trình cơ bản về môn học mà bạn chọn',
        'Từ đó bạn có thể tự luyện tập với máy ở chế độ AI và phát triển bản thân những kỹ năng riêng biệt của mình'
        
        ]),
    is_activating = False
)
intensive_course.save()

advance_course = Course(
    name = "Advance",
    fee = 100,
    time = "14 Buổi",
    content = ['Combat 1 vs 1 cùng giảng viên', 'Trao đổi tự do thoải mái không giới hạn','Trong các giờ học sẽ tổ chức các cặp thi đấu với nhau',
    'Hướng dẫn cơ bản và các kỹ năng cao cấp và sắp xếp các chế độ chơi giữa các học viên với nhau, từ đó học viên sẽ cải thiện được bản thân về lối chơi, chiến thuật riêng mình',
    'khi bạn bước ra khỏi lớp học sẽ tự tin đi du đấu với những người chơi khác để nâng cao level'    
    ],
    is_activating = False
)
advance_course.save()



# Lecturer List

esport_lecturer = Lecturer(
    name = 'Nguyễn Minh Quang',
    phone_number = '01655181694',
    email = 'cuccungcuaem@gmail.com',
    specialized = 'E-Sport'
)
esport_lecturer.save()

music_lecturer = Lecturer(
    name = 'Đỗ Bích Ngọc',
    phone_number = '0123665996',
    email = 'tiennudangyeu210@gmail.com',
    specialized = 'Music'
)
music_lecturer.save()

music_lecture = Lecturer(
    name = 'Doãn Huy Hoàng',
    phone_number = '01655232114',
    email = 'namthandeptrai@gmail.com',
    specialized = 'Music'
)
music_lecturer.save()

art_lecturer = Lecturer(
    name = 'Nguyễn Trà My',
    phone_number = '0169554333',
    email = 'tiennuxungxinh912@gmail.com',
    specialized = 'Art'
)
art_lecturer.save()

art_lecturer = Lecturer(
    name = 'Nguyễn Mỹ Linh',
    phone_number = '0945553333',
    email = 'tiennuxundep64@gmail.com',
    specialized = 'Art'
)
art_lecturer.save()
