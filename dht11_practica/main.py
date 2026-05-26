import time
from dht_reader import LectorDHT11
import sensor_utils

def main():
    # Instanciamos el lector de nuestro archivo dht_reader
    lector = LectorDHT11()
    print("Iniciando lectura del DHT11...")
    print("Presiona Ctrl+C en cualquier momento para detener.\n")
    
    try:
        while True:
            # 1. Leer los datos del hardware
            temp_c, humedad = lector.leer()
            
            # 2. Usar las funciones auxiliares
            temp_f = sensor_utils.celsius_a_fahrenheit(temp_c)
            mensaje = sensor_utils.dar_formato_impresion(temp_c, temp_f, humedad)
            
            # 3. Mostrar en consola
            print(mensaje)
            
            # El DHT11 necesita mínimo 2 segundos de descanso entre lecturas
            time.sleep(2.0)
            
    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")
    finally:
        lector.limpiar()
        print("Sensor desconectado de forma segura.")

if __name__ == "__main__":
    main()
