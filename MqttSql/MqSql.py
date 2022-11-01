from paho.mqtt import client as mqtt_client
import time
from TesteSQL import DataBase

broker = 'node02.myqtthub.com'
port = 1883
topicot1 = 'machali1231/escritorio/st1'
topicoh1 = 'machali1231/escritorio/sh1'
client_id = 'python'
username = 'python1901'
password = 'cpce1901'

conectado = False
recivido = False
topicos = [topicot1, topicoh1]
datos = []
lecturas = {}


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado a broker")
        global conectado
        conectado = True
    else:
        print("Failed to connect, return code %d\n", rc)


def on_mesasage(client, userdata, msg):
    # print("mensaje recibido: " + str(msg.payload.decode("utf-8")))
    lec = str(msg.payload.decode("utf-8"))
    datos.append(lec)


client = mqtt_client.Client(client_id)
client.on_message = on_mesasage
client.username_pw_set(username, password)
client.connect(broker, port)
client.on_connect = on_connect

for t in topicos:
    client.subscribe(t)

client.loop_start()
while not conectado:
    time.sleep(0.2)
while not recivido:
    time.sleep(0.2)
    if not datos or len(datos) < len(topicos):
        pass
    else:
        lecturas = dict(zip(topicos, datos))
        database = DataBase()
        database.grabar('st1', (float(lecturas[topicot1])))
        database.grabar('sh1', (float(lecturas[topicoh1])))
        database.cerrar()
        datos = []

client.loop_stop()
print("Cerrado")
