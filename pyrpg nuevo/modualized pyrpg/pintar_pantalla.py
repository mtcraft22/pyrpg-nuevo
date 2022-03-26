import os
import time

import pintar_vara_vida

piso = 45
aciones = ["atacar", "esquivar"]


def actualizar_pantalla(aciones):
    os.system("cls")
    print(" ")
    print(" ", end="")
    pintar_vara_vida.draw_hp_bar(40, 5, 2)
    print("")
    print("                                           ", " Enemigo:", end=" ")
    print(" [█████]")
    print("----------------------------------------------------------------")
    print(f" Piso: {piso}")
    print("----------------------------------------------------------------")
    print(" Aciones: ")
    a = 1
    for i in aciones:
        print(" ", a, ". ", i)
        a += 1


actualizar_pantalla(aciones)
aciones.append("objecto")
time.sleep(5)
actualizar_pantalla(aciones)
