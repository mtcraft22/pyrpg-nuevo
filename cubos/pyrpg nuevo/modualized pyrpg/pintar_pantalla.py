import os
import platform
import time

import classes_entidades  # classes de los personajes del juego
import indicar_acion  # modulo para la decteció de la ación a realizar
import pintar_vara_vida  # importacion de modulo para mostrar la vara de vida dinamica

piso = 1
aciones = ["atacar", "esquivar", "burla"]


def actualizar_pantalla(aciones, comentario):
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

    print(" ")
    print(" ", end="")
    pintar_vara_vida.draw_hp_bar(classes_entidades.Marc.vida_maxima,
                                 classes_entidades.Marc.vida_actual,
                                 classes_entidades.Marc.name)
    print("")
    print("                                           ", " Enemigo:", end=" ")
    pintar_vara_vida.draw_hp_bar(classes_entidades.Random_tick_speed.vida_maxima,
                                 classes_entidades.Random_tick_speed.vida_actual,
                                 classes_entidades.Random_tick_speed.name)
    print("----------------------------------------------------------------")
    print(f" Piso: {piso}")
    print("----------------------------------------------------------------")
    print(" Aciones: ")
    a = 1
    for i in aciones:
        print(" ", a, ". ", i)
        a += 1
    print("----------------------------------------------------------------")
    print(f"Ultimo evento: {comentario}")
    print("----------------------------------------------------------------")


actualizar_pantalla(aciones, "")
aciones.append("objecto")
time.sleep(2)
actualizar_pantalla(aciones, "")
if indicar_acion.preguntar_acion(aciones) == 0:
    classes_entidades.Marc.acer_daño(classes_entidades.Random_tick_speed)
    actualizar_pantalla(aciones, "ataque con exito")
else:
    actualizar_pantalla(aciones, "acion sin soporte, "
                                 f"num acion: {indicar_acion.preguntar_acion(aciones)}")
print("gracias por jugar")
