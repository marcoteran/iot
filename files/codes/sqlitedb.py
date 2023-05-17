# Importación de bibliotecas necesarias
import sqlite3
import Adafruit_DHT
import time
from datetime import datetime

# Definición del tipo de sensor y el pin al que está conectado
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Asume que el sensor está en el pin 4

# Creación de la conexión a la base de datos
conn = sqlite3.connect('dht11_data.db')

# Creación de un cursor
c = conn.cursor()

# Creación de la tabla de la base de datos (si no existe)
c.execute('''
    CREATE TABLE IF NOT EXISTS dht11_data (
        timestamp TEXT,
        temperature NUMERIC,
        humidity NUMERIC
    )
''')

while True:
    # Lectura de los datos del sensor
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        # Obtención de la fecha y hora actuales
        now = datetime.now()

        # Inserción de los datos en la base de datos
        c.execute("INSERT INTO dht11_data VALUES (?, ?, ?)",
                  (now.strftime("%Y-%m-%d %H:%M:%S"), temperature, humidity))

        # Guardado de los cambios
        conn.commit()

        time.sleep(1)  # Tiempo de espera antes de la próxima lectura
    else:
        print("Failed to retrieve data from humidity sensor")

# Cierre de la conexión a la base de datos
conn.close()