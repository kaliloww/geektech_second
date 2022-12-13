# Тема
# def printe(name):
#     print(f"{name} its may name")
# printe("nurtilek")


# class Cars:
#     motor= 1
#     def __init__(self , model , age ,marca) -> None:
#         self.model = model
#         self.age = age
#         self.marca = marca
#     def __str__(self) -> str:
#         return f'{self.model}\n'\
#                f'{self.age}\n '\
#                f'{self.marca}'
# car1= Cars("BMW", 2012 , "M5")
# # print(car1.marca ,car1.age , car1.marca )
# print(car1)

# class Human:

#     # атрибуты уровня класса
#     head =1
#     hand =2
#     def __init__(self , name ,age) -> None:
#         self.name = name
#         self.age= age
#     def printt(self):
#         print(self.name,  "is run")


# beka = Human('beka' , 20)
# beka.printt()
# nurbek1 = Human("Nurbek" , 18)
# nurbek1.printt()


# huma = Human("Nurtilek" , 19)
# print(huma.name , huma.age)
# human_1 = Human("Abdulla" , 32)
# print(human_1.name , human_1.age)
# print(human_1.hand)

class human:
    def __init__(self , name , age) -> None:
        self.name = name 
        self.age = age
class Run:
    def run(self,name):
        print(name,"is runn")
hum = human("Nurti" , 19)
Run.run(hum.name)


# homework
class SuperHero:
    people = "people"
    def __init__(self , people) -> None:
        print(people)
human=SuperHero(people=)