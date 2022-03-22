class Entidad:
	def __init__(self,nombre, vida=20, ataque=2):
		self.vida_maxima=vida
		self.vida_actual=vida
		self.ataque=ataque
		self.name= nombre
	def recibir_daño(self):
		self.vida_actual -= 5

Random_tick_speed = Entidad("Random_tick_speed",ataque=1)
Marc= Entidad("Marc")
