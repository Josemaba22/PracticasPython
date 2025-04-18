import threading
import time

def tarea(nombre):
    for i in range(3):
        print(f"Hilo {nombre} - Iteración {i}")
        time.sleep(2)

# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("A"))
hilo2 = threading.Thread(target=tarea, args=("B"))

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que terminen
hilo1.join()
hilo2.join()

print("¡Todos los hilos han terminado!")
