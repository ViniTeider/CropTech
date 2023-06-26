from models import db, Sensor, Section, Plantation, Client
from collections import defaultdict
from datetime import datetime

class Read(db.Model):
    __tablename__ = "reads"
    id = db.Column("id", db.Integer(), primary_key=True)
    section_id = db.Column("section_id", db.Integer(), db.ForeignKey(Section.id), nullable=False)
    sensor_id = db.Column("sensor_id", db.Integer(), db.ForeignKey(Sensor.id), nullable=False)
    value = db.Column("value", db.Float(), nullable=False, default=0.0)
    date_time = db.Column("date_time", db.DateTime(), nullable=False, default=datetime.now())

    def get_reads():
        reads = Read.query.join(Section, Section.id == Read.section_id).join(Sensor, Sensor.id == Read.sensor_id)\
                    .add_columns(Read.id,Read.section_id,Section.name,Read.sensor_id,Sensor.measure,Read.value,Read.date_time).all()

        return reads

    def save_read(section_id,sensor_id,value,date_time):
        read = Read(section_id = section_id, sensor_id = sensor_id, value = value, date_time = date_time)

        db.session.add(read)
        db.session.commit()

    def get_plants(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id).join(Read, Read.section_id == Section.id) \
                            .add_columns(Section.id.label("section_id"), Section.name.label("section_name"), Plantation.name.label("plantation_name"), Plantation.id.label("plantation_id"), Client.id.label("client_id"), Read.sensor_id, Read.value) \
                            .filter(Client.id == id, Read.sensor_id.in_([1, 2, 4]))

        sections_per_plantation = defaultdict(lambda: defaultdict(dict))
        for plant in plants:
            sections_per_plantation[plant.plantation_id][plant.section_id]["section_id"] = plant.section_id
            sections_per_plantation[plant.plantation_id][plant.section_id]["section_name"] = plant.section_name
            sections_per_plantation[plant.plantation_id][plant.section_id]["plantation_name"] = plant.plantation_name
            sections_per_plantation[plant.plantation_id][plant.section_id]["plantation_id"] = plant.plantation_id
            sections_per_plantation[plant.plantation_id][plant.section_id]["client_id"] = plant.client_id
            if plant.sensor_id == 1:
                sections_per_plantation[plant.plantation_id][plant.section_id]["umidade"] = plant.value
            elif plant.sensor_id == 2:
                sections_per_plantation[plant.plantation_id][plant.section_id]["temperatura"] = plant.value
            elif plant.sensor_id == 4:
                sections_per_plantation[plant.plantation_id][plant.section_id]["luz"] = plant.value

        return sections_per_plantation


'''
    def get_plants(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id).join(Read, Read.section_id == Section.id) \
                            .add_columns(Section.id.label("section_id"), Section.name.label("section_name"), Plantation.name.label("plantation_name"), Plantation.id.label("plantation_id"), Client.id.label("client_id")) \
                            .filter(Client.id == id) \
                            .add_columns(Read.value.label("umidade"), Read.value.label("temperatura"), Read.value.label("luz")) \
                            .filter(Client.id == id, Read.sensor_id.in_([1, 2, 4]))

        sections_per_plantation = defaultdict(list)
        for plant in plants:
            sections_per_plantation[plant.plantation_id].append(plant)

        return sections_per_plantation
'''


'''
    def get_plants(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id).join(Read, Read.section_id == Section.id)\
                            .add_columns(Section.id.label("section_id"),Section.name.label("section_name"),Plantation.name.label("plantation_name"),Plantation.id.label("plantation_id"),Client.id.label("client_id"))\
                            .filter(Client.id == id)\
                            .add_columns(Read.value.label("umidade"))\
                            .filter(Client.id == id).filter(Read.sensor_id == 1)\
                            .add_columns(Read.value.label("temperatura"))\
                            .filter(Client.id == id).filter(Read.sensor_id == 2)\
                            .add_columns(Read.value.label("luz"))\
                            .filter(Client.id == id).filter(Read.sensor_id == 4)

        sections_per_plantation = defaultdict(list)
        for plant in plants:
            sections_per_plantation[plant.plantation_id].append(plant)

        return sections_per_plantation

    def get_umidity(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id).join(Read, Read.section_id == Section.id)\
                            .add_columns(Read.value.label("umidade"))\
                            .filter(Client.id == id).filter(Read.sensor_id == 1)

        sections_per_plantation_umidity = defaultdict(list)
        for plant in plants:
            sections_per_plantation_umidity[plant.plantation_id].append(plant)

        return sections_per_plantation_umidity

    def get_temperature(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id).join(Read, Read.section_id == Section.id)\
                            .add_columns(Plantation.id.label("plantation_id"),Read.value.label("temperatura"))\
                            .filter(Client.id == id).filter(Read.sensor_id == 2)

        sections_per_plantation_temperature = defaultdict(list)
        for plant in plants:
            sections_per_plantation_temperature[plant.plantation_id].append(plant)

        return sections_per_plantation_temperature

    def get_light(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id).join(Read, Read.section_id == Section.id)\
                            .add_columns(Plantation.id.label("plantation_id"),Read.value.label("luz"))\
                            .filter(Client.id == id).filter(Read.sensor_id == 4)

        sections_per_plantation_light = defaultdict(list)
        for plant in plants:
            sections_per_plantation_light[plant.plantation_id].append(plant)

        return sections_per_plantation_light
'''