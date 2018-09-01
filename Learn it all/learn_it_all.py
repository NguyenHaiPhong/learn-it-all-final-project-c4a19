import mlab
from models.classes import *
from datetime import datetime
from flask import *
lia_app = Flask(__name__)

mlab.connect()
lia_app.secret_key = "lia"

#. Homepage
@lia_app.route("/")
def homepage():
    return render_template("homepage.html")

#. Show all customers (Admin)
@lia_app.route("/user/admin/show-all-customers")
def show_all_customers():
    if "user_signed_in" in session:
        user_id = session["user_signed_in_id"]
        user = User.objects.with_id(user_id)
        if user[0].is_admin == True:
            all_customers = User.objects(is_admin = False)
            return render_template("show-all-customers.html", all_customers = all_customers)
        elif user[0].is_admin == False:
            return ("Bạn không có quyền đăng nhập.")

#. Show all courses 
@lia_app.route("/show-all-categories")
def show_all_courses():
    if "user_signed_in" in session:
        music = Category.objects(name = "Music")
        sport = Category.objects(name = "Sport")
        esport = Category.objects(name = "E-Sport")
        return render_template("show-all-categories.html", music = music)
    else:
        return redirect(url_for("user_sign_in"))

#. Courses info
@lia_app.route("/show-all-courses/courses-info/")
def course_info():
    if "user_signed_in" in session:
        return render_template("course-info.html")
    else:
        return redirect(url_for("user_sign_in"))

#. Courses detail
# @lia_app.route("/show-all-courses/courses-info/courses-detail/<course_id>")
# def course_detail(course_id):


#. Course detail
# @lia_app.route("/show-all-courses/courses-info/course-detail")
# def course_detail(course_id):
#     if "user_signed_in" in session:
#         course = Course.ojects.
#         return render_template("course-detail.html", course = course)
#     else:
#         return redirect(url_for("user_sign_in"))

#. User sign in
@lia_app.route("/user/user-sign-in", methods = ["GET", "POST"])
def user_sign_in():
    if request.method == "GET":  
        if "user_signed_in" in session:
            return redirect(url_for("homepage"))
        else:
            return render_template("user/user-sign-in.html")
    elif request.method == "POST":
        form = request.form
        sign_in = form["sign-in"]
        password = form["password"]
        all_customers = User.objects(sign_in = sign_in, 
        password = password)
        if len(all_customers) != 0:
            user_id = all_customers[0].id
            session["user_signed_in"] = True
            session["user_signed_in_id"] = str(user_id)
            if all_customers[0].is_admin == True:
                return render_template("admin.html")
            elif all_customers[0].is_admin == False:
                return redirect(url_for("homepage"))
        elif len(all_customers) == 0:
            return ("Sai tài khoản.")

#. Update course (Admin)
@lia_app.route("/user/admin/update-course/<course_id>", methods = ["GET", "POST"])
def update_course(course_id):
    all_courses = Course.objects.with_id(course_id)
    if len(all_courses) != 0:
        if request.method == "GET":
            if "admin_signed_in" in session:
                return render_template("update-course.html", all_courses = all_courses)
            else:
                return redirect(url_for("admin_sign_in"))
        elif request.method == "POST":
            form = request.form     
            name = form["name"]
            fee = form["fee"]
            content = form["content"]
            is_activating = form["is_activating"]
            if is_activating == "Còn hoạt động":
                checking = True
            elif is_activating == "Không còn hoạt động":
                checking = False
            update_course = all_courses[0]
            update_course.update(set__name = name, set__fee = fee,
            set__content = content, set__is_activating = checking)
    elif len(all_courses) == 0:
        return ("Khoá học hiện không còn khả dụng.")

#. Show all orders
@lia_app.route("/user/admin/show-all-orders")
def show_all_orders():
    if "admin_signed_in" in session:
        all_orders = Order.objects()
        return render_template("orders-page.html", all_orders = all_orders)
    else:   
        return redirect(url_for("admin_sign_in"))

#. Accept order
@lia_app.route("/user/admin/accept-orders/<order_id>/<course_id>")
def accept_orders(order_id, course_id):
    if "admin_signed_in" in session:
        order = Order.objects.with_id(order_id)
        if len(order) != 0:
            course = Course.objects.with_id(course_id)
            if len(course) != 0:
                order.update(set__is_purchased = True)
                return ("Đã phê duyệt.")    
            elif len(course) == 0:
                return ("Khoá học hiện không còn khả dụng.")
        elif len(order) == 0:
            return redirect(url_for(""))

#. Customer profile 
@lia_app.route("/user/customer/customer-profile")
def customer_profile():  
        if "customer_signed_in" in session:
            return render_template("customer-profile.html")
        else:
            return render_template("customer-sign-in.html")

#. Customer sign up
@lia_app.route("/user-sign-up", methods = ["GET", "POST"])
def customer_sign_up():
    if request.method == "GET":
        return render_template("customer-sign-up.html")
    elif request.method == "POST":
        form = request.form
        sign_up = form["sign-up"]
        email = form["email"]
        password = form["password"]
        new_customer = User(
            sign_in = sign_up,
            email = email,
            password = password,
        )
        new_customer.save()
        return redirect(url_for("customer_sign_in"))

#. Detail Course (Customer)
@lia_app.route("/course/detail/<course_id>")
def course_detail(course_id):
    all_courses = Course.objects.with_id(course_id)
    if len(all_courses) != 0:
        if "customer_signed_in" in session:
            course = all_courses[0]
            return render_template("course-detail.html", course = course)
        else:
            return redirect(url_for("customer_sign_in"))
    elif len(all_courses) == 0:
        return ("Khoá học hiện tại không khả dụng.")

#. Order course 
@lia_app.route("/course/order-course/<course_id>/<customer_id>")
def order_service(course_id, customer_id):
    if "customer_signed_in" in session:
        order = Order.objects(course_id = course_id, customer_id = customer_id)
        if len(order) == 0:
            new_order = Order(
                course_id = course_id,
                customer_id = customer_id,
                order_time = datetime.now(),
                is_purchased = False
            )
            new_order.save()
            return ("Đã gửi yêu cầu.")
        elif len(order) != 0:
            return ("Bạn đã gửi yêu cầu. Xin chờ xác nhận.")

#. Customer sign out
@lia_app.route("/customer/customer-sign-out")
def customer_sign_out():
    if "user_signed_in" in session:
        del session['user_signed_in']
        return redirect(url_for("homepage"))
  
if __name__ == '__main__':
    lia_app.run(debug=True)

 