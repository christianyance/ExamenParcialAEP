#Hacer que el sistema genere un numero aleatorio entre 1 y 10. Luego hacer que el usuario adivine el numero.La aplicacion debe terminar cuando el usuario adivine

import random

s = random.randint(1,100)

while True:
    n = int(input("Adivina el numero del sistema (1...10):"))
    if n == s:
        print("Adivinaste")
        break
    else:
        print("Numero incorrecto")
