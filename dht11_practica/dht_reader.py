import adafruit_dht
import board

class LectorDHT11:
    def __init__(self, pin=board.D4):
        # Inicializa el sensor en el GPIO 4 (Pin físico 7)
        self.sensor = adafruit_dht.DHT11(pin)
        
    def leer(self):
        try:
            temp = self.sensor.temperature
            hum = self.sensor.humidity
            return temp, hum
        except RuntimeError:
            # Los DHT11 suelen fallar en algunas lecturas, es normal.
            return None, None
        except Exception as error:
            self.sensor.exit()
            raise error
            
    def limpiar(self):
        self.sensor.exit()
