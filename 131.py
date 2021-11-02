#cd D:python/python
#131.py
#Напишите объявление класса JetPlane, который наследуется от Rocket и AirPlane?

class Rocket:

	def __init__(self, fuil, metal):
		self.fuil = fuil
		self.metal=metal

	def print1(self):
		print ("Топливо: ")
		return (str(self.fuil + " л"))

class Airplane:

	def __init__(self, speed):
		self.speed = speed

	def print2(self):
		print ("Скорость: ")
		return (str(self.speed) +  " км/час")

class JetPlane(Rocket, Airplane):
	def __init__(self, fuil, speed, metal, country):
		super(JetPlane,self).__init__(fuil=fuil, metal=metal)
		Airplane.__init__(self, speed=speed)
		self.country = country

	def print(self):
		print("\n")
		print("Создан с: " + self.metal)
		print("Топливо: " + self.fuil + " л")
		print("Скорость: " + self.speed + " км/час")
		return (str("Страна: " + self.country))

m = input("С какго метала сделан: ")
f = input("Топливо: ")
s = input("Скорость: ")
c = input("Страна: ")

jatplane = JetPlane(f,s,m,c)
print(jatplane.print())