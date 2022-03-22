import pintar_vara_vida #importacion de modulo para mostrar la vara de vida dinamica
import indicar_acion    # modulo para la decteció de la ación a realizar
import classes_entidades # classes de los personajes del juego
import os
import time

piso = 1
aciones = ["atacar", "esquivar"]


def actualizar_pantalla(aciones):
    os.system("cls")
    print(" ")
    print(" ", end="")
    pintar_vara_vida.draw_hp_bar(classes_entidades.Marc.vida_maxima,classes_entidades.Marc.vida_actual,classes_entidades.Marc.name)
    print("")
    print("                                           ", " Enemigo:", end=" ")
    pintar_vara_vida.draw_hp_bar(classes_entidades.Random_tick_speed.vida_maxima,classes_entidades.Random_tick_speed.vida_actual,classes_entidades.Random_tick_speed.name)
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
indicar_acion.preguntar_acion(aciones)

