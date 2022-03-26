class Entidad:
    def __init__(self, nombre, vida=20, ataque=2):
        self.vida_maxima = vida
        self.vida_actual = vida
        self.ataque = ataque
        self.name = nombre

    def acer_daño(self, destino):
        destino.vida_actual -= self.ataque


Random_tick_speed = Entidad("Random_tick_speed", ataque=1)
Marc = Entidad("Marc")
