from flask import Blueprint, render_template,redirect,url_for, request
from models import Sensor, Actuator
from flask_login import current_user, login_required

iot = Blueprint("iot", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@iot.route("/")
@login_required
def iot_index():
    return render_template("/iot/iot_index.html", name = current_user.username)

@iot.route("/register_sensor")
@login_required
def register_sensor():
    return render_template("/iot/register_sensor.html", name = current_user.username)

@iot.route("/view_sensors")
@login_required
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors = sensors, name = current_user.username)

@iot.route("/save_sensors", methods = ["POST"])
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description ,voltage, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))

@iot.route("/update_registered_sensor/id=<int:id>")
@login_required
def update_registered_sensor(id):
    id = id
    return render_template("/iot/update_registered_sensor.html", id=id, name = current_user.username)

@iot.route("/update_sensor/", methods = ["POST"])
def update_sensor():
    id = request.form.get("id")
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.update_sensor(id, name, brand, model, description ,voltage, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))

@iot.route("delete_sensor/id=<int:id>")
def delete_sensor(id):
    id = id
    Sensor.delete_sensor(id)

    return redirect(url_for('admin.iot.view_sensors'))

@iot.route("/register_actuator")
@login_required
def iot_register_actuator():
    return render_template("/iot/register_actuator.html", name = current_user.username)

@iot.route("/view_actuators")
@login_required
def iot_view_actuators():
    actuators = Actuator.get_actuators()
    return render_template("/iot/view_actuators.html", actuators=actuators, name = current_user.username)

@iot.route("/save_actuators", methods = ["POST"])
def save_actuator():
    name = request.form.get("name", None)
    model = request.form.get("model", None)
    brand = request.form.get("brand", None)
    voltage = request.form.get("voltage", None)
    description = request.form.get("description", None)
    is_active = True if request.form.get("is_active", None) == "on" else False

    Actuator.save_actuator(name,model,brand,voltage,description,is_active)

    return redirect(url_for("admin.iot.iot_view_actuators"))

@iot.route("/update_registered_actuator/id=<int:id>")
@login_required
def update_registered_actuator(id):
    id = id
    return render_template("/iot/update_registered_actuator.html", id=id, name = current_user.username)

@iot.route("/update_actuator/", methods = ["POST"])
def update_actuator():
    id = request.form.get("id")
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Actuator.update_actuator(id, name, brand, model, description ,voltage, is_active)

    return redirect(url_for('admin.iot.iot_view_actuators'))

@iot.route("delete_actuator/id=<int:id>")
def delete_actuator(id):
    id = id
    Actuator.delete_actuator(id)

    return redirect(url_for('admin.iot.iot_view_actuators'))