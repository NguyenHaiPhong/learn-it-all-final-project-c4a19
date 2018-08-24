from mongoengine import *
from models.models import *
from datetime import datetime
from faker import Faker as fake
import mlab

mlab.connect()

new_admin = User(
    name = "admin",
    email = "thelivingdeath.n2h.destroyer@gmail.com",
    phone_number = "123456789",
    sign_in = "admin",
    password = "admin",    
    is_activating = True,
    is_admin = True
)
new_admin.save()