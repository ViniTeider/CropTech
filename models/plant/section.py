from collections import defaultdict
from models import db, Plantation, Client

class Section(db.Model):
    __tablename__ = "sections"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    plantation_id = db.Column(db.Integer, db.ForeignKey(Plantation.id))

    def save_section(name,plantation_id):
        section = Section (name = name, plantation_id = plantation_id)

        db.session.add(section)
        
        db.session.commit()

    def get_sections():
        sections = Section.query.join(Plantation, Plantation.id == Section.plantation_id)\
                        .add_columns(Plantation.name.label("plantation_name"), Section.id, Section.name.label("section_name")).all()
        return sections
    
    def delete_section(id):
        section = Section.query.filter(Section.id == id).first()
        db.session.delete(section)
        db.session.commit()

    def update_section(id, name):
        Section.query.filter_by(id=id)\
                .update(dict(name = name))

        db.session.commit()

    def get_plants(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id)\
                                        .add_columns(Section.id.label("section_id"),Section.name.label("section_name"),Plantation.name.label("plantation_name"),Plantation.id.label("plantation_id"),Client.id.label("client_id"))\
                                        .filter(Client.id == id)
        
        sections_per_plantation = defaultdict(list)
        for plant in plants:
            sections_per_plantation[plant.plantation_id].append(plant)


        return sections_per_plantation