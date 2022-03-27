import file_manipulation

enemigos = []
enemigos_probabilidad = []
for i in file_manipulation.Padre_Enemies.enemies_cargados:
    enemigos.append(file_manipulation.Padre_Enemies.enemies_cargados[i]["name"] + ".json")

for i in enemigos:
    for a in range(file_manipulation.Padre_Enemies.enemies_cargados[i]["weight"]):
        enemigos_probabilidad.append(i)

'''class Entidad: # classe de enemigos de debug
    def __init__(self, nombre, vida=20, ataque=2):
        self.vida_maxima = vida
        self.vida_actual = vida
        self.ataque = ataque
        self.name = nombre

    def acer_daño(self, destino):
        destino.vida_actual -= self.ataque'''

# < instancias debug>
'''Random_tick_speed = Entidad("Random_tick_speed", ataque=1)
Marc = Entidad("Marc")'''
# </instancias debug>
