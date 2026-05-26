def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    if celsius is not None:
        return (celsius * 9/5) + 32
    return None

def dar_formato_impresion(temp_c, temp_f, humedad):
    """Genera el texto bonito para la terminal."""
    if temp_c is not None and humedad is not None:
        return f"🌡️ Temp: {temp_c:.1f}°C ({temp_f:.1f}°F)  |  💧 Humedad: {humedad}%"
    else:
        return "⏳ Fallo en la lectura. Reintentando..."
