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

#. User sign in
@lia_app.route("/customer/customer-sign-in", methods = ["GET", "POST"])
def user_sign_in():
    error = None
    if request.method == "GET":  
        if "user_signed_in" in session:
            return redirect(url_for("homepage"))
        else:
            return render_template("user/user-sign-in.html")
    elif request.method == "POST":
        form = request.form
        sign_in = form["sign-in"]
        password = form["password"]
        all_users = User.objects(sign_in__exact = sign_in, 
        password__exact = password)
        if len(all_users) != 0:
                user_id = all_users[0].id
                session["user_signed_in"] = True
                session["user_signed_in_id"] = str(user_id)
                if all_users[0].is_admin:
                    return redirect(url_for("admin_page"))
                else:
                    return redirect(url_for("homepage"))
        elif len(all_users) == 0:
            flash("Wrong username or password")
            error = 'Sai Tài Khoản'
            return render_template("user/user-sign-in.html", error = error)

# ---ADMIN---
#. Admin page
@lia_app.route("/user/admin")
def admin_page():
    if "user_signed_in" in session:
        user_id = session["user_signed_in_id"]
        user = User.objects.with_id(user_id)
        if user.is_admin:
            return render_template("user/admin/admin.html")
        else:
            return redirect(url_for("homepage"))
    else:
        return render_template("user/user-sign-in.html")

#. Show all lecturers
@lia_app.route("/user/admin/show-all-lecturers")
def admin_show_all_lecturers():
    if "user_signed_in" in session:
        user_id = session["user_signed_in_id"]
        user = User.objects.with_id(user_id)
        if user.is_admin:
            all_lecturers = Lecturer.objects()
            return render_template("user/admin/show-all-lecturers.html", 
            all_lecturers = all_lecturers)
        elif user.is_admin == False:
            return ("Bạn không có quyền truy cập.")

#. Show all customers
@lia_app.route("/user/admin/show-all-customers")
def admin_show_all_customers():
    if "user_signed_in" in session:
        user_id = session["user_signed_in_id"]
        user = User.objects.with_id(user_id)
        if user.is_admin:
            all_customers = User.objects(is_admin = False)
            return render_template("user/admin/show-all-customers.html", 
            all_customers = all_customers)
        else:
            return ("Bạn không có quyền truy cập.")

#. Show all orders
@lia_app.route("/user/admin/show-all-orders")
def admin_show_all_orders():
    if "user_signed_in" in session:
        user_id = session["user_signed_in_id"]
        user = User.objects.with_id(user_id)
        if user.is_admin:
            all_orders = Order.objects()
            return render_template("orders-page.html", 
            all_orders = all_orders)
        else:
            return redirect(url_for("homepage"))
    else:   
        return render_template("user/user-sign-in.html")

#Show all courses
@lia_app.route("/user/admin/show-all-courses")
def admin_show_all_courses():
    if "user_signed_in" in session:
        use_id = session["user_signed_in_id"]
        user = User.objects.with_id(use_id)
        if user.is_admin:
            all_courses = Course.objects()
            return render_template("user/admin/show-all-courses.html", 
            all_courses = all_courses)
        else:
            return redirect(url_for("homepage"))
    else:
        return render_template("user/user-sign-in.html")

#. Update lecturer
@lia_app.route("/user/admin/update-lecturer/<lecturer_id>", methods = ["GET", "POST"])
def admin_update_lecturer(lecturer_id):
    if request.method == "GET":
        if "user_signed_in" in session:
            use_id = session["user_signed_in_id"]
            user = User.objects.with_id(use_id)
            if user.is_admin:
                lecturer = Lecturer.objects.with_id(lecturer_id)
                return render_template("update-lecturer.html", lecturer = lecturer)
            else:
                return redirect(url_for("user_sign_in"))
    elif request.method == "POST":
        form = request.form     
        name = form["name"]
        email = form["email"]
        height = form["height"]
        weight = form["weight"]
        phone_number = form["phone_number"]
        description = form["description"]
        is_activating = form["is-activating"]
        if is_activating == "Còn hoạt động":
            checking = True
        elif is_activating == "Không còn hoạt động":
            checking = False
        update_lecturer = lecturer
        update_lecturer.update(set__name = name, set__email = email,
        set__height = height, set__weight = weight, set__phone_number = phone_number, 
        set__description = description, set__is_activating = checking)
        return redirect(url_for("admin_show_all_lecturers"))

#. Update course
@lia_app.route("/user/admin/update-course/<course_id>", methods = ["GET", "POST"])
def update_course(course_id):
    if request.method == "GET":
        if "user_signed_in" in session:
            use_id = session["user_signed_in_id"]
            user = User.objects.with_id(use_id)
            if user.is_admin:
                course = Course.objects.with_id(course_id)
                return render_template("update-course.html", course = course)
        else:
            return redirect(url_for("user_sign_in"))
    elif request.method == "POST":
        form = request.form     
        name = form["name"]
        level = form["level"]
        fee = form["fee"]
        description = form["description"]
        detail = form["detail"]
        duration = form["duration"]
        schedule_time = form["schedule-time"]
        is_activating = form["is-activating"]
        if is_activating == "Còn hoạt động":
            checking = True
        elif is_activating == "Không còn hoạt động":
            checking = False
        update_course = all_courses[0]
        update_course.update(set__name = name, set__level = level,
        set__fee = fee, set__description = description, set__detail = detail, set__duration = duration, 
        set__schedule_time = schedule_time, set__is_activating = checking)
        return redirect(url_for("admin_show_all_courses"))

#. Delete lecturer
@lia_app.route("/user/admin/del-lecturer/<lecturer_id>")
def admin_del_lecturer(lecturer_id):
    if "user_signed_in" in session:
        use_id = session["user_signed_in_id"]
        user = User.objects.with_id(use_id)
        if user.is_admin:
            lecturer = Lecturer.objects.with_id(lecturer_id)
            update_lecturer = lecturer
            update_lecturer.update(set__is_activating = False)
            return redirect(url_for("admin_show_all_lecturers"))

#. Accept order
@lia_app.route("/user/admin/show-all-orders/accept-order/<order_id>")
def admin_accept_orders(order_id):
    if "user_signed_in" in session:
        user_id = session["user_signed_in_id"]
        user = User.objects.with_id(user_id)
        if user.is_admin:
            order = Order.objects.with_id(order_id)
            accept_order = order
            accept_order.update(set__is_purchased = True)
            return ("Đã phê duyệt.")    
        else:
            return redirect(url_for("homepage"))        
    else:   
        return render_template("user/user-sign-in.html")

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

# ---CUSTOMER---
#. Show all categories
@lia_app.route("/show-all-categories")
def show_all_categories():
    all_categories = Category.objects()
    return render_template("show-all-categories.html", all_categories = all_categories)

#. Courses info
@lia_app.route("/show-all-courses/courses-info/")
def course_info():
    if "user_signed_in" in session:
        return render_template("course-info.html")
    else:
        return redirect(url_for("user_sign_in"))

#. Customer profile 
@lia_app.route("/user/customer-profile")
def customer_profile():
    if "user_signed_in" in session:
        customer_id = session["user_signed_in_id"]
        customer = User.objects.with_id(customer_id)
        return render_template("user/customer-profile.html", customer = customer)
    else:
        return redirect(url_for("user_sign_in"))

#. Customer sign up
@lia_app.route("/user/user-sign-up", methods = ["GET", "POST"])
def customer_sign_up():
    error = None
    if request.method == "GET":
        return render_template("user/user-sign-up.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        email = form["email"]
        sign_up = form["sign_up"]
        password = form["password"]
        new_customer = User(
            sign_in = sign_up,
            email = email,
            password = password,
        )
        # print(new_customer)
        new_customer.save()
        return redirect(url_for("customer_sign_in"))

#. Detail Course (Customer)
@lia_app.route("/course/detail/<course_id>")
def course_detail(course_id):
    # all_courses = Course.objects.with_id(course_id)
    course = Course.objects.with_id(course_id)
    if len(course) != 0:
        if "customer_signed_in" in session:
            return render_template("course_detail.html", course = course)
        else:
            return redirect(url_for("customer_sign_in"))
    elif len(course) == 0:
        return ("Khoá học hiện tại không khả dụng.")

#. Order course 
@lia_app.route("/course/order-course/<course_id>/<customer_id>")
def order_service(course_id, customer_id):
    if "user_signed_in" in session:
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

#. User sign out
@lia_app.route("/customer/customer-sign-out")
def customer_sign_out():    
    if "user_signed_in" in session:
        del session['user_signed_in']
        return redirect(url_for('homepage'))

# ---PAGE---
@lia_app.route("/esport")
def esport():
    return render_template('esport.html')

# route PES
@lia_app.route('/esport/pes')
def pes():
   return render_template ('what-is-pes.html')

@lia_app.route('/pes/basic')
def basic_learning_pes():
    return render_template('basic-learning-pes.html')
    
# route DOTA2
@lia_app.route('/esport/dota2')
def dota2():
    return render_template('what-is-dota2.html')

@lia_app.route('/dota2/basic')
def basic_learning_dota2():
    return render_template('basic-learning-dota2.html')

# route LOL
@lia_app.route('/esport/lol')
def lol():
    return render_template('what-is-lol.html')

@lia_app.route('/dota2/lol')
def basic_learning_lol():
    return render_template ('basic-learning-lol.html')

# route Music
@lia_app.route('/music')
def music():
    return render_template('music-course.html')

if __name__ == '__main__':
    lia_app.run(debug=True)

 