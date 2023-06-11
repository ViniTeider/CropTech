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
    

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#                                            TRABALHAR NESSA QUERY DPS
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

    def get_umidity(id):
        plants = Section.query.join(Plantation, Plantation.id == Section.plantation_id).join(Client, Client.id == Plantation.client_id)\
                    .join(Read, Read.section_id == Section.id).join(Sensor, Sensor.id == Read.sensor_id)\
                    .add_columns(Plantation.id.label("plantation_id"), Read.value.label("value"))\
                    .filter(Client.id == id).filter(Sensor.id == 1)\
                    .order_by(Read.date_time.desc()).all()
        
        sections_per_plantation = defaultdict(list)
        for plant in plants:
            sections_per_plantation[plant.plantation_id].append(plant)

        return sections_per_plantation