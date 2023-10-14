import threading
from pyModbusTCP.client import ModbusClient
from time import sleep
import cv2

# Función para la visión artificial
def vision_artificial(modbus_client):
    # Cargar el clasificador de cascada
    cascade = cv2.CascadeClassifier("cascade.xml")

    # Configurar la URL de la cámara IP
    camara = 0
    cap = cv2.VideoCapture(camara)

    signal = ""

  

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error al leer el fotograma de la cámara")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        try:
            # Detectar objetos utilizando el clasificador de cascada
            # ajustes de sencibilidad
            # valor 1.0 sera mas lento y mas preciso set: 1.05 , valor 4 numero de vecino 5 sera mas lento y mas acertado, valor 100 area minima
            stop = cascade.detectMultiScale(gray, 1.02, 4, 100)

            if len(stop):
                signal = "stop"
                for x, y, w, h in stop:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            else:
                signal = "no hay objeto"
        except:
            print("No se ha logrado acceder al clasificador de cascada")

        if signal == "stop":
            print("Stop")
            # Aquí puedes escribir el valor deseado en el registro Modbus
            # Por ejemplo, escribir el valor 1 en el registro 0:
            modbus_client.write_single_register(0, 1)
        else:
            print("No hay objeto")
            modbus_client.write_single_register(0, 0)

        cv2.imshow("img", frame)

        key = cv2.waitKey(10)
        if key & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# Función para la conexión a Modbus
def modbus():
    slave_address = "192.168.2.10"
    port = 502
    id_slave = 1

    try:
        mod_client = ModbusClient(
            host=slave_address,
            port=port,
            unit_id=id_slave,
            auto_open=True,
        )

        print("Conectado a Modbus")
    except:
        print("No se pudo conectar a Modbus")
        return

    vision_artificial(mod_client)

if __name__ == "__main__":
    # Crear un hilo para la conexión a Modbus
    hilo_modbus = threading.Thread(target=modbus)

    # Iniciar el hilo Modbus
    hilo_modbus.start()

    # Esperar a que el hilo Modbus termine (esto nunca ocurrirá en este ejemplo)
    hilo_modbus.join()
