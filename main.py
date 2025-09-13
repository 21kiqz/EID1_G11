
import os
import sys
from interfaz import main_gui

def hay_entorno_grafico():
    
    if sys.platform.startswith("win") or sys.platform == "darwin":
        return True
    return os.environ.get("DISPLAY") is not None

if __name__ == "__main__":
    if hay_entorno_grafico():
        main_gui()
    else:
        print("No se detectó entorno gráfico. La interfaz solo funciona en sistemas con GUI (Windows, macOS, o Linux con entorno gráfico).")
