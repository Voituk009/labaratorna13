#cd D:python/python
#133.py
#Напишите программу, в которой классы Car и 
#Bus будут производными от класса Transport, 
#а MicroBus – производным от  Car и Bus. 
#Сделайте Transport абстрактным типом данных с 
#двумя чисто виртуальными функциями. 
#Классы Car и Bus не должны быть ADT. 
#Проверьте программу, путем создания объектов разных типов.

class Transport: #клас транспорт

	def set(self, number, date, mark): #конструктор
		self._protected_member = number
		self._protected_member = date
		self._protected_member = mark


	def __init__(self, number, date, mark): 
		self.number = number
		self.date = date
		self.mark = mark

	def print(self): #Метод вывода на экран
		print("\n")
		print ("Номер:", self.number)
		print ("Год выпуска: ", self.date)
		print ("Марка: ")
		return self.mark


class Car(Transport): #класс автомобиль

	def __init__(self, speed):
		self.speed = speed

	def printcar(self):
		print("Максимальная скорость: ")
		return (str(self.speed) + " км/час")


class Bus(Transport): #класс автобус

	def __init__(self, seats):
		self.seats = seats

	def printbus(self):
		print("Число посадочных мест: ")
		return self.seats

 #класс микроавтобус
class  Microbus(Car, Bus):
	def __init__(self, number, date, mark, speed, seats):
		super(Microbus,self).__init__(speed=speed)
		Bus.__init__(self, seats=seats)
		self.number=number
		self.date=date
		self.mark=mark

	def print(self):
		print("\n")
		print ("Номер:", self.number)
		print ("Год выпуска: ", self.date)
		print ("Марка: ", self.mark)
		print ("Максимальная скорость: ", self.speed,  " км/час")
		return("Число посадочных мест: " + str(self.seats))
		
		
a = int(input ("Номер: "))
b = int(input ("Год выпуска: "))
c = str(input ("Марка: "))
d = int(input ("1 - если машина, 0 - если автобус, если 2 микроавтобус: "))

Tr = Transport(a, b, c) 

if int(d) == 1: #Создание транспорта автомобил

	x = int(input ("Максимальная скорость: "))
	print (Tr.print())
	Cr = Car(x)
	print (Cr.printcar())

elif int(d) == 0: #Создание транспорта автобус

	y = int(input ("Число посадочных мест: "))
	print (Tr.print())
	Bs = Bus(y)
	print (Bs.printbus())
 
elif int(d) == 2: #Создание транспорта микроавтобус

	f = int(input ("Максимальная скорость: "))
	g = int(input ("Число посадочных мест: "))
	McBs1 = Microbus(a,b,c,f,g)
	print(McBs1.print())