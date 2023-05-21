from models.db import db, instance

from models.auth.role import Role
from models.auth.user import User
from models.auth.user_roles import UserRole

from models.people.person import Person
from models.people.employee import Employee
from models.people.client import Client 

from models.plant.plantation import Plantation
from models.plant.section import Section

from models.iot.device import Device
from models.iot.sensor import Sensor
from models.iot.actuator import Actuator
from models.iot.read import Read
from models.iot.activation import Activation
