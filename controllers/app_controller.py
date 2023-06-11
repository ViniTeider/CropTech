from flask import Flask, render_template, session, g
from controllers.admin_controller import admin
from controllers.auth_controller import auth
from flask_login import LoginManager

from datetime import datetime

from models import Read


from models.mqtt import mqtt_client, topic_subscribe

from models.db import db, instance 

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", 
                        static_folder="./static/", 
                        root_path="./")

    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance

    #inicialização MQTT
    app.config['MQTT_BROKER_URL'] = 'broker.emqx.io'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_PASSWORD'] = ''  # Set this item when you need to verify username and password
    app.config['MQTT_KEEPALIVE'] = 5  # Set KeepAlive time in seconds
    app.config['MQTT_TLS_ENABLED'] = False  # If your broker supports TLS, set it True
    app.config["SQLALCHEMY_DATABASE_URI"] = instance

    mqtt_client.init_app(app)


    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/admin')


    @app.route('/')
    def index():
        return render_template("home.html")



    #Rotas do MQTT
    @mqtt_client.on_connect()
    def handle_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connected successfully')
            for topic in topic_subscribe:   
                mqtt_client.subscribe(topic) # subscribe topic
        else:
            print('Bad connection. Code:', rc)

    @mqtt_client.on_message()
    def handle_mqtt_message(client, userdata, message):
        data = dict(
            topic=message.topic,
            payload=message.payload.decode()
        )
        
        if(message.topic in ["/CropTech/infoUmidade"]):
            with app.app_context():
                umidade = message.payload.decode()
                reads = Read(section_id = 3, sensor_id = 1, value = umidade, date_time=datetime.now())
                db.session.add(reads)
                db.session.commit()

        if(message.topic in ["/CropTech/infoTemperatura"]):
            with app.app_context():
                infoTemperatura = message.payload.decode()
                reads = Read(section_id = 3, sensor_id = 2, value = infoTemperatura, date_time=datetime.now())
                db.session.add(reads)
                db.session.commit()

        if(message.topic in ["/CropTech/infoLuz"]):
            with app.app_context():
                infoLuz = message.payload.decode()
                reads = Read(section_id = 3, sensor_id = 4, value = infoLuz, date_time=datetime.now())
                db.session.add(reads)
                db.session.commit()

        if(message.topic in ["/CropTech/infoEstadoAgua"]):
            infoEstadoAgua = message.payload.decode()
            print(infoEstadoAgua)

        print('Received message on topic: {topic} with payload: {payload}'.format(**data))

    
    return app