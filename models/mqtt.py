from flask_mqtt import Mqtt

mqtt_client = Mqtt()
topic_subscribe = ["/CropTech/infoUmidade", "/CropTech/infoTemperatura", "/CropTech/infoLuz", "/CropTech/infoEstadoAgua"]
#esta sem o topico de ativação ( "/CropTech/comando")