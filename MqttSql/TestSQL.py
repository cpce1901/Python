import pymysql


class DataBase:
    def __init__(self):
        self.cconnection = pymysql.connect(
            host='201.148.104.122',
            user='automat2_claudio',
            password='1-j(D3wgOgB*',
            db='automat2_Test'
        )

        try:
            self.cursor = self.cconnection.cursor()
            print("Conexion realizada")
        except Exception as e:
            raise print("fallo en la conexion")

    def grabar(self, tabla, dato):
        sql = "INSERT INTO {} (dato) VALUES ({})".format(tabla, dato)

        try:
            self.cursor.execute(sql)
            self.cconnection.commit()
            print("Dato grabado")

        except Exception as e:
            raise print("No ha sido posible grabar el dato")

    def leer_todo(self):
        sql = " SELECT * FROM Sensor"

        try:
            self.cursor.execute(sql)
            leer = self.cursor.fetchall()

            for i in leer:
                print("id:", i[0])
                print("temperatura:", i[1])
                print("registro:", i[2])
                print("-------------\n")

        except Exception as e:
            raise

    def cerrar(self):
        self.cconnection.close()


