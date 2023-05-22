from flask import Blueprint, render_template, redirect,url_for
from flask_login import current_user, login_required
#from flask_user import roles_required
from controllers.people_controller import people
from controllers.iot_controller import iot
from controllers.plant_controller import plant
from models import Section

admin = Blueprint("admin", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

admin.register_blueprint(people, url_prefix='/people')
admin.register_blueprint(iot, url_prefix='/iot')
admin.register_blueprint(plant, url_prefix='/plant')

@admin.route("/")
@admin.route("/admin")
@login_required
#@roles_required('admin')
def admin_index():
    if not current_user.is_authenticated:
        return redirect(url_for("auth.login"))
    else:
        if(current_user.role == 'admin'):
            return render_template("admin/admin_index.html", name = current_user.username)
        else:
            sections_per_plantation = Section.get_plants(current_user.id)
            
            return render_template("client/view_plants.html", sections_per_plantation = sections_per_plantation, name = current_user.username)
        
    
    