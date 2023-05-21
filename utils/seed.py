from models import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def generate_seeds(db:SQLAlchemy):
    
    role1 = Role(name='admin')
    role2 = Role(name='client')

    db.session.add_all([role1,role2])
    db.session.commit()
    
    user1 = User(email = "a@a", username = "Vina", password = generate_password_hash("a"))
    user2 = User(email = "b@b", username = "Hask", password = generate_password_hash("b"))
    user3 = User(email = "c@c", username = "Predo", password = generate_password_hash("c"))
    user4 = User(email = "d@d", username = "Brono", password = generate_password_hash("d"))
    user5 = User(email = "e@e", username = "Antonio", password = generate_password_hash("e"))

    user1.roles = [role1]
    user2.roles = [role2]
    user3.roles = [role1]
    user4.roles = [role2]
    user5.roles = [role2]

    db.session.add_all([user1,user2,user3,user4,user5])
    db.session.commit()

    #Pessoa (cliente e funcionario)

    person1 = Person(name = "Vina", cpf = 1234567891, email = "a@a", senha="1234", birth_date='2023-05-21')
    person2 = Person(name = "Hask", cpf = 534314321, email = "b@b", senha="1234", birth_date='2023-05-21')
    person3 = Person(name = "Predo", cpf = 99876544321, email = "c@c", senha="1234", birth_date='2023-05-21')
    person4 = Person(name = "Brono", cpf = 6543452341, email = "d@d", senha="1234", birth_date='2023-05-21')

    db.session.add_all([person1,person2,person3,person4])
    db.session.commit()

    client1 = Client(id = person1.id)
    client2 = Client(id = person2.id)
    funcionario1 = Employee(id = person3.id)
    funcionario2 = Employee(id = person4.id)

    db.session.add_all([client1,client2,funcionario1,funcionario2])
    db.session.commit()


    #Plantas

    plantation1 = Plantation(name = 'plantacao 1', client_id = client1.id)
    plantation2 = Plantation(name = 'plantacao 2', client_id = client1.id)
    plantation3 = Plantation(name = 'plantacao 3', client_id = client2.id)

    db.session.add_all([plantation1,plantation2,plantation3])
    db.session.commit()

    section1 = Section(name = 'trigo', plantation_id = plantation1.id)
    section2 = Section(name = 'arroz', plantation_id = plantation1.id)
    section3 = Section(name = 'arroz', plantation_id = plantation2.id)
    section4 = Section(name = 'batata', plantation_id = plantation3.id)
    section5 = Section(name = 'cenoura', plantation_id = plantation3.id)

    db.session.add_all([section1,section2,section3,section4,section5])
    db.session.commit()



    #IOT

    device1 = Device(brand = "ESP32", model = "ESP32", name = "Umidade", voltage = 5, description = "Sendor de umidade com medida em percentual")
    device2 = Device(brand = "ESP32", model = "ESP32", name = "Temperatura", voltage = 5, description = "Sendor de temperatura com unidade de medida em graus celsios")
    device3 = Device(brand = "ESP32", model = "ESP32", name = "Infravermelhor", voltage = 5, description = "Sendor de pequenas distâncias infravermelho")
    device4 = Device(brand = "ESP32", model = "ESP32", name = "Luminosidade", voltage = 5, description = "Sendor de luminosidade (LDR)")
    device5 = Device(brand = "ESP32", model = "ESP32", name = "Movimento/Presença", voltage = 5, description = "Sendor de movimento/presença, retornando booleano pra detecção ou não de objetos em movimento")
    device6 = Device(brand = "ESP32", model = "ESP32", name = "Lampada LED", voltage = 5, description = "Atuador - Lâmpada led")
    device7 = Device(brand = "ESP32", model = "ESP32", name = "Motor Corrente Contínua", voltage = 5, description = "Motor de corrente contínua com caixa de redução")
    device8 = Device(brand = "ESP32", model = "ESP32", name = "Motor de Passo", voltage = 5, description = "Motor de passo para tarefas específicas e com precisão de movimento")
    device9 = Device(brand = "ESP32", model = "ESP32", name = "Servo Motor", voltage = 5, description = "Servo motor para movimentos específicos 180 graus")

    db.session.add_all([device1, device2, device3, device4, device5,device6,device7,device8,device9])
    db.session.commit()

    sensor1 = Sensor(id = device1.id, measure = "%")
    sensor2 = Sensor(id = device2.id, measure = "ºC")
    sensor3 = Sensor(id = device3.id, measure = "cm")
    sensor4 = Sensor(id = device4.id, measure = "Lumens")
    sensor5 = Sensor(id = device5.id, measure = "")

    db.session.add_all([sensor1, sensor2, sensor3, sensor4, sensor5])
    db.session.commit()

    actuator1 = Actuator(id = device6.id, actuator_type = None)
    actuator2 = Actuator(id = device7.id, actuator_type = "Chassi Robótico")
    actuator3 = Actuator(id = device8.id, actuator_type = "ULN2003")
    actuator4 = Actuator(id = device9.id, actuator_type = None)

    db.session.add_all([actuator1, actuator2, actuator3, actuator4])
    db.session.commit()
    
