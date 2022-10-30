import paho.mqtt.client as mqtt
import pymysql


class DataBase:
    def __init__(self):
        self.cconnection = pymysql.connect(
            host='localhost',
            user='root',
            password='cpce1901',
            db='Demo'
        )

        try:
            self.cursor = self.cconnection.cursor()
            print("Conexion realizada")
        except:
            print("fallo en la conexion")

    def crear(self, dato):
        try:
            dato = float(dato)
            sql = "INSERT INTO datos (Temp) VALUES ({})".format(dato)
            
            try:
                self.cursor.execute(sql)
                self.cconnection.commit()
                print("Ingresado")
            except:
                print("Hubo un error")
        
        except:
            print("El valor no es posible de procesar")
        

    def cierre(self):
        self.cconnection.close()


class Mqtt(DataBase):
    client = mqtt.Client()

    def __init__(self, broker, usuario, clave, puerto, tiempo, topico):
        self. broker = broker
        self.usuario = usuario
        self.clave = clave
        self.puerto = puerto
        self.tiempo = tiempo
        self.topico = topico
        super().__init__()

    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(self.topico)

    def on_message(self, client, userdata, msg):
        lectura = str(msg.payload)
        lectura = lectura[2:-1]   
        lectura = lectura.replace("\\", "").replace("n","")        
        self.crear(lectura)        
        print(lectura)

    def conexion(self):
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(self.broker, self.puerto, self.tiempo)

    def lectura_siempre(self):
        self.client.loop_forever()

    def detener_lectura(self):
        self.client.loop_stop()


mq = Mqtt("broker.hivemq.com", "cpce1901", "cpce1901", 1883, 60, "machali1231")
mq.conexion()
mq.lectura_siempre()
