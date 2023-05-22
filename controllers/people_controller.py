from flask import Blueprint, render_template,redirect,url_for,request
from models import Client,Employee
from datetime import datetime
from flask_login import current_user, login_required

people = Blueprint("people", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@people.route("/")
@login_required
def people_index():
    return render_template("/people/people_index.html",  name = current_user.username)

@people.route("/register_client")
@login_required
def people_register_client():
    return render_template("/people/register_client.html",  name = current_user.username)

@people.route("/view_clients")
@login_required
def people_view_clients():
    clients = Client.get_clients()
    return render_template("/people/view_clients.html", clients=clients,  name = current_user.username)

@people.route("/save_client", methods = ['POST'])
def save_client():
    name = request.form.get("name",None)
    cpf = request.form.get("cpf",None)
    email = request.form.get("email",None)
    senha = request.form.get("senha",None)
    birth_date = request.form.get("birth_date",None)
    created_at = datetime.today()

    Client.save_client(name,cpf,email,senha,birth_date,created_at)

    return redirect(url_for("admin.people.people_view_clients"))

@people.route("/update_registered_client/id=<int:id>")
@login_required
def update_registered_client(id):
    id = id
    return render_template("/people/update_registered_client.html", id=id,  name = current_user.username)

@people.route("/update_client/", methods = ["POST"])
def update_client():
    id = request.form.get("id")
    name = request.form.get("name",None)
    cpf = request.form.get("cpf",None)
    email = request.form.get("email",None)
    senha = request.form.get("senha",None)
    birth_date = request.form.get("birth_date",None)
    created_at = datetime.today()

    Client.update_client(id, name,cpf,email,senha,birth_date,created_at)

    return redirect(url_for('admin.people.people_view_clients'))

@people.route("delete_client/id=<int:id>")
def delete_client(id):
    id = id
    Client.delete_client(id)

    return redirect(url_for('admin.people.people_view_clients'))

@people.route("/register_employee")
@login_required
def people_register_employee():
    return render_template("/people/register_employee.html",  name = current_user.username)

@people.route("/view_employees")
@login_required
def people_view_employees():
    employees = Employee.get_employees()
    return render_template("/people/view_employees.html", employees=employees,  name = current_user.username)

@people.route("/save_employee", methods = ['POST'])
def save_employee():
    name = request.form.get("name",None)
    cpf = request.form.get("cpf",None)
    email = request.form.get("email",None)
    senha = request.form.get("senha",None)
    birth_date = request.form.get("birth_date",None)

    Employee.save_employee(name,cpf,email,senha,birth_date)

    return redirect(url_for("admin.people.people_view_employees"))

@people.route("/update_registered_employee/id=<int:id>")
@login_required
def update_registered_employee(id):
    id = id
    return render_template("/people/update_registered_employee.html", id=id,  name = current_user.username)

@people.route("/update_employee/", methods = ["POST"])
def update_employee():
    id = request.form.get("id")
    name = request.form.get("name",None)
    cpf = request.form.get("cpf",None)
    email = request.form.get("email",None)
    senha = request.form.get("senha",None)
    birth_date = request.form.get("birth_date",None)

    Employee.update_employee(id, name,cpf,email,senha,birth_date)

    return redirect(url_for('admin.people.people_view_employees'))

@people.route("delete_employee/id=<int:id>")
def delete_employee(id):
    id = id
    Employee.delete_employee(id)

    return redirect(url_for('admin.people.people_view_employees'))