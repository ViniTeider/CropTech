from models import db, Client, Person

class Plantation(db.Model):
    __tablename__ = "plantations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    client_id = db.Column(db.Integer, db.ForeignKey(Client.id))

    def save_plantation(name,client_id):
        plantation = Plantation (name = name, client_id = client_id)

        db.session.add(plantation)
        
        db.session.commit()

    def get_plantations():
        plantations = Plantation.query.join(Client, Client.id == Plantation.client_id)\
                        .join(Person, Person.id == Client.id)\
                        .add_columns(Plantation.id,Plantation.name.label("plantation_name"),Person.name.label("person_name")).all()
        
        return plantations

    def delete_plantation(id):
        plantation = Plantation.query.filter(Plantation.id == id).first()
        db.session.delete(plantation)
        db.session.commit()

    def update_plantation(id, name):
        Plantation.query.filter_by(id=id)\
                .update(dict(name = name))

        db.session.commit()