from models import db, Device

class Actuator(db.Model):
    __tablename__ = "actuators"
    id = db.Column("actuator_id", db.Integer(), db.ForeignKey(Device.id), primary_key=True)
    actuator_type = db.Column(db.String(30))

    activations = db.relationship("Activation", backref="actuators", lazy=True)

    def save_actuator(name, model, brand, voltage, description, is_active):
        device = Device(name = name, 
                        model = model, 
                        brand = brand, 
                        voltage = voltage, 
                        description = description, 
                        is_active = is_active)
        
        actuator = Actuator(id = device.id)
        
        device.actuators.append(actuator)

        db.session.add(device)
        db.session.commit()

    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id == Actuator.id)\
                        .add_columns(Device.id, Device.name, Device.model,
                                     Device.brand, Device.voltage, Device.description,
                                     Device.is_active).all()
        
        return actuators
    
    def delete_actuator(id):
        actuator = Actuator.query.filter(Actuator.id == id).first()
        db.session.delete(actuator)
        db.session.commit()

    def update_actuator(id, name, brand, model, description, voltage, is_active):
        Device.query.filter_by(id=id)\
                .update(dict(name = name, brand=brand, model = model, 
                        voltage = voltage, description = description, 
                        is_active = is_active))

        db.session.commit()