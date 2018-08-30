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

#. Admin sign in
@lia_app.route("/admin/admin-sign-in",  methods = ["GET", "POST"])
def admin_sign_in():
    if request.method == "GET":
        if "admin_signed_in" in session:
            return render_template("admin.html")  
        else:
            return render_template("admin-sign-in.html")
    elif request.method == "POST":
        form = request.form
        sign_in = form["sign-in"]
        password = form["password"]
        admin = User.objects(sign_in__exact = sign_in, 
        password__exact = password, is_admin = True)
        if len(admin) != 0:
            admin_id = admin[0].id
            session["admin_signed_in"] = True
            session["admin_signed_in_id"] = str(admin_id)
            return render_template("admin.html")  
        elif len(admin) == 0: 
            return ("Sai tài khoản.")

#. Show all customers (Admin)
@lia_app.route("/admin/show-all-customers", )
def show_all_customers():
    if "admin_signed_in" in session:
        all_customers = User.objects(is_admin = False)
        return render_template("all-customers.html", all_customers = all_customers)
    else:
        return render_template("admin-sign-in.html")

#. Show all courses (Admin)
@lia_app.route("/admin/show-all-courses")
def show_all_courses():
    if "admin_signed_in" in session:
        all_courses = Course.objects()
        return render_template("all-courses.html", all_courses = all_courses)
    else:
        return render_template("admin-sign-in.html")

#. Update course (Admin)
@lia_app.route("/admin/update-course/<course_id>", methods = ["GET", "POST"])
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
@lia_app.route("/admin/show-all-orders")
def show_all_orders():
    if "admin_signed_in" in session:
        all_orders = Order.objects()
        return render_template("orders-page.html", all_orders = all_orders)
    else:   
        return redirect(url_for("admin_sign_in"))

#. Accept order
@lia_app.route("/admin/accept-orders/<order_id>/<course_id>")
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

#. Admin sign out
@lia_app.route("/admin/admin-sign-out")
def admin_sign_out():
    del session["admin_signed_in"]
    return redirect(url_for("homepage"))

#. Customer profile 
@lia_app.route("/customer/customer-profile/<customer_id>")
def customer_profile(customer_id):
    if "customer_signed_in" in session:
        customer = User.objects.with_id(customer_id)
        return render_template("detail.html", customer = customer)
    else:
        return redirect(url_for("customer_sign_in"))

#. Customer sign in
@lia_app.route("/customer/customer-sign-in", methods = ["GET", "POST"])
def customer_sign_in():
    if request.method == "GET":  
        if "customer_signed_in" in session:
            return redirect(url_for("customer_profile"))
        else:
            return render_template("customer-sign-in.html")
    elif request.method == "POST":
        form = request.form
        sign_in = form["sign_in"]
        password = form["password"]
        all_customers = User.objects(sign_in__exact = sign_in, 
        password__exact = password, is_admin = False)
        if len(all_customers) != 0:
            customer_id = all_customers[0].id
            session["customer_signed_in"] = True
            session["customer_signed_in_id"] = str(customer_id)
            return redirect(url_for("customer_profile"))
        elif len(all_customers) == 0:
            return ("Sai tài khoản.")

#. Customer sign up
@lia_app.route("/customer/customer-sign-up", methods = ["GET", "POST"])
def customer_sign_up():
    if request.method == "GET":
        return render_template("customer-sign-up.html")
    elif request.method == "POST":
        form = request.form
        name = form["name"]
        email = form["email"]
        sign_up = form["sign-up"]
        password = form["password"]
        new_customer = User(
            name = name,
            email = email,
            sign_in = sign_up,
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
    if "customer_signed_in" in session:
        del session['customer_signed_in']
        return redirect(url_for('homepage.html'))
  
if __name__ == '__main__':
    lia_app.run(debug=True)

 