import time
from lcd_display import LCD

def main():
    lcd = LCD()
    
    while True:
        print("\n" + "="*35)
        print("    MENÚ DE CONTROL LCD I2C")
        print("="*35)
        print("1. Mostrar Reloj Dinámico (Infinito)")
        print("2. Mensaje con Scroll Horizontal")
        print("3. Salir")
        print("="*35)
        
        opcion = input("Elige una opción (1-3): ")
        
        try:
            if opcion == '1':
                print("Mostrando reloj... (Presiona Ctrl+C para regresar)")
                while True:
                    hora_actual = time.strftime("%H:%M:%S")
                    fecha_actual = time.strftime("%d/%m/%Y")
                    lcd.write(f"Hora:  {hora_actual}", f"Fecha: {fecha_actual}")
                    time.sleep(1)
                    
            elif opcion == '2':
                texto = input("Escribe el mensaje largo para el scroll: ")
                print("Ejecutando scroll en la pantalla...")
                lcd.scroll_text(texto, delay=0.2)
                
            elif opcion == '3':
                print("Saliendo del programa...")
                break
                
            else:
                print("Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Regresando al menú...")
            lcd.clear()

    lcd.clear()
    lcd.close()
    print("LCD apagado correctamente.")

if __name__ == "__main__":
    main()
