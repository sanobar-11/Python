#
#
# class BankAccaunt:
#     def __init__(self, name, balance=0):
#         self.name=name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance += amount
#     def cash(self,amount):
#         self.balance -=amount
#     def my_balance(self):
#         return self.balance
# client_name = input ('vvedite svoe imya:')
# client1 = BankAccaunt(client_name)
# while True:
#     choice = int(input('1-depozit, 2-obnalichit, 3-balans'))
#     if choice == 1:
#         how_much= int(input('summa depozita: '))
#         client1.depozite(how_much)
#     elif choice == 2:
#         how_much = int (input('summa vivoda: '))
#         client1.cash(how_much)
#     elif choice == 3:
#         print(client1.my_balance())


# class Car:
#     def __init__ (self,model,color,year):
#         self.model=model
#         self.color=color
#         self.year=year
#     def stop(self):
#         print('mashina ostanovilas')
#     def change_color (self,new_color):
#         self.color = new_color
# gentra= Car('ravon', 'black' , 2022)
#
# gentra.change_color('red')
# print(gentra.color)
#
# def x(values):
#     values[0]=1
# v = [10,9,8]
# x (v)
# print(v)

#
# class Animal:
#     def make_sound(self, s):
#         print(s)
#
# class Horse(Animal):
#     def dibi(self):__
#         print ('vstal na dibi')
# giraffe = Animal()
# mustang = Horse()
# mustang.make_sound ('igogo')
# mustang.dibi()
# giraffe.dibi()


#
#
# class (Car):
#     def __init__ (self,model,color,year):
#         self.model =model
#         self.color =color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__ (self,model,color,year,sponsor):
#         super.__init__(model,color,year)
#         self,sponsor = sponsor
#
# kia = Car('Chevrolet', 'White', 2024)
# amgone = SuperCar('BWM', 'Gold', 2025, 'Petronas')
# print(amgone)


#
# class MyClass:
#     def __init__ (self,value):
#         self.value = value
#         @classmethod
#         def from_sting(cls,string):
#             return cls(int(sting))
# my_obj = MyClass.from_string ("11")
# print(my_obj.value)
#

#
# class Rectangle:
#     def __init__ (self, width, height):
#         self.width=width
#         self.height=height
#     @property
#     def area (self):
#         return self.width + self.height
#
# rectangle = Rectangle(4,5)
# print(rectangle.area) #vivod:20
# rectangle.widht=6
# print(rectangle.area) #vivod 30
#

#
# class Worker:
#     def __init__ (self, name, position):
#         self.name= name
#         self.position=position
#
#     def work(self):
#         print('rabotayet')
#
# class HR(Worker):
#     def __init__(self,name,position):
#         super(). __init__ (name,position)
#     def show_info(self,worker):
#         return worker.position
# sanobar = Worker('SHAXZOD', 'Junior')
# sarvinoz = HR('SANOBAR', 'HR')
#
# sanobar.work()
# print(sarvinoz.show_info(sanobar))



