from flask import Blueprint, render_template,redirect,url_for,request
from models import Plantation,Section, Read
from models import Client
from datetime import datetime,date
from flask_login import current_user, login_required
from models.mqtt import mqtt_client


plant = Blueprint("plant", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")


#ROTAS DO CLIENTE

@plant.route("/client")
@login_required
def client_index():
    sections_per_plantation = Section.get_plants(current_user.id)
    print(sections_per_plantation)

    umidity = Read.get_umidity(current_user.id)
    print("\n\n\n\n")
    print(umidity)
    print("\n\n\n\n")

    return render_template("/client/view_plants.html", sections_per_plantation = sections_per_plantation, name = current_user.username, umidity = umidity)

@plant.route("/client/register_plant")
@login_required
def client_register_plant():
    return render_template("/client/register_plant.html",name = current_user.username)



#ROTAS DO ADMIN

@plant.route("/")
@login_required
def plant_index():
    return render_template("/plant/plant_index.html",  name = current_user.username)

@plant.route("/register_plantation")
@login_required
def plant_register_plantation():
    return render_template("/plant/register_plantation.html",  name = current_user.username)

@plant.route("/view_plantations")
@login_required
def plant_view_plantations():
    plantations = Plantation.get_plantations()
    return render_template("/plant/view_plantations.html", plantations=plantations,  name = current_user.username)

@plant.route("/save_plantation", methods = ['POST'])
def save_plantation():
    name = request.form.get("name",None)
    client_id = request.form.get("client_id",None)

    Plantation.save_plantation(name, client_id)

    return redirect(url_for("admin.plant.plant_view_plantations"))

@plant.route("/update_registered_plantation/id=<int:id>")
@login_required
def update_registered_plantation(id):
    id = id
    return render_template("/plant/update_registered_plantation.html", id=id,  name = current_user.username)

@plant.route("/update_plantation/", methods = ["POST"])
def update_plantation():
    id = request.form.get("id")
    name = request.form.get("name")

    Plantation.update_plantation(id, name)

    return redirect(url_for('admin.plant.plant_view_plantations'))

@plant.route("delete_plantation/id=<int:id>")
def delete_plantation(id):
    id = id
    Plantation.delete_plantation(id)

    return redirect(url_for('admin.plant.plant_view_plantations'))



@plant.route("/register_section")
@login_required
def plant_register_section():
    return render_template("/plant/register_section.html",  name = current_user.username)

@plant.route("/view_sections")
@login_required
def plant_view_sections():
    sections = Section.get_sections()
    return render_template("/plant/view_sections.html", sections=sections,  name = current_user.username)

@plant.route("/save_section", methods = ['POST'])
def save_section():
    name = request.form.get("name",None)
    plantation_id = request.form.get("plantation_id",None)

    Section.save_section(name, plantation_id)

    return redirect(url_for("admin.plant.plant_view_sections"))



@plant.route("/update_registered_section/id=<int:id>")
@login_required
def update_registered_section(id):
    id = id
    return render_template("/plant/update_registered_section.html", id=id,  name = current_user.username)

@plant.route("/update_section/", methods = ["POST"])
def update_section():
    id = request.form.get("id")
    name = request.form.get("name")

    Section.update_section(id, name)

    return redirect(url_for('admin.plant.plant_view_sections'))

@plant.route("delete_section/id=<int:id>")
def delete_section(id):
    id = id
    Section.delete_section(id)

    return redirect(url_for('admin.plant.plant_view_sections'))