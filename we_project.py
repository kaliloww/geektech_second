# # import random
# lose = 0
# win = 0
# while True:# print("a b c f")

    # user_hod = input("камень ножницы или бумага ?")
    # hod = ["Камень" ,"Ножница", "Бумага"]
    # random_number = random.choice(hod)
   
    # 
    # if user_hod == "Камень" and random_number == "Ножницы" :
        # print(f"Выигрышь!!!бот выбрал {random_number}")
        # win+=1
    # elif user_hod == "Камень" and random_number=="Бумага":
        # print(f"Проигрыш ): бот выбрал {random_number}")
        # lose+=1
    # elif user_hod == "Ножницы" and random_number == "Камень" :
        # print(f"Проигрыш ): бот выбрал {random_number}")
        # lose +=1
    # elif user_hod == "Ножницы" and random_number == "Бумага":
        # print(f"Выигрышь!!!бот выбрал {random_number}")
        # win+=1
    # elif user_hod == "Бумага" and random_number=="Камень":
    #     print(f"Выигрышь!!!бот выбрал {random_number}")
    #     win+=1
    # elif user_hod == "Бумага" and random_number == "Ножницы":
    #     print(f"Проигрыш ): бот выбрал {random_number}")
        # lose+=1
    # elif random_number == user_hod:
    #     print(f"ничья оба выбрали {random_number}")
    #     win+=1  
    #     lose+=1
    # else:
    #     print("Ошибка")
    # print(f'win= {win}')
    # print(f'lose= {lose}')
    # if win >= 5 :
    #     print(f"вы выиграли со счётом {win}:{lose}")
    #     break
    # elif lose >= 5:
    #     print(f"Вы проиграли со счётом {lose}:{win}")
    #     # break
    
# tupl = (1,2,44,64,65)  #type = tuple (кортеж)
# five = 5
# two = 4
# one = 1
# s = (five  ,  two  , one)
# print(s)

# tupl =(1,"Nurtilek", 25.0 , True)
# # print(tupl[0:2])
# a,b,c,d = (12,"cdvcdsv",2.2,False)
# print(a)
# name = "Nurti"
# age = 19
# (age ,name)= ("Nurti",19)
# print(age)
# setq = {1,2,2,3,2,4,4,12,23,"Nurtilek"}
# print(setq)

# пусть есть два списка, и нужно отыскать и вывести их одинаковые компоненты
# unbreakable_diamond = ['Jotaro', 'Josuke', 'Koichi']
# golden_wind = ['Jotaro', 'Koichi', 'Giorno']
# & - здесь оператор пересечения
# overlap = set(unbreakable_diamond) & set(golden_wind)
# print(overlap)
# letter =word[2]
# print(letter)
# d = {"a":"s" ,"b":"t"}
# s = {"a":"t" ,"b":"s" }
# d.update(s)
# print(d)
# a = ["baha","nurik","adi","kesha","aiba"]
# a.sort()
# c = a[::-1]
# a.reverse()
# print(a==c , a is c)



# рппп лоборатория pro=
# print("x y z f g")
# for x in (0,1):
#     for y in (0,1):
#         for z in (0,1):
#             f=((x or y)or z)<= ((x or y) and(x or z))
#             g =  x or (y ==z)
#             print(x,y,z,f,g)
# if f==g:
#     print(True)
# else:
#     print(False)

# print("x y z f g")
# for x in (0,1):
#     for y in (0,1):
#         for z in (0,1):
#             f = (x or y)and (y or z)
#             g = (x or y or z)and (x or y or z)and(x or y or z)
#             print(x, y ,z,f ,g)
# if f==g:
#     print(True)
# else:
#     print(False)

# class SuperHero:
#     people = 'people'
#     def __init__(self , name,nickname,superpower,health_points,catchphrase) -> None:
#         self.name= name
#         self.nicname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchphrase = catchphrase
#     def __str__(self ) -> str:
#         return f'name is {self.name}\nnicname is {self.nicname}\nsuperpower is {self.superpower}\nhealth_points is {self.health_points}\ncatchphrase is {self.catchphrase}'
#     def healthPoints(self):
#         print(f"if we multiply the hero's health_points by 2 then we get {int(self.health_points)*2}")
#     def catchPhrase(self):
#         print(len(self.catchphrase))
        
# hero = SuperHero("Nurtilek","Nurti","comp","100","Лучшее конечно впереди")
# print(hero)
# hero.healthPoints()
# hero.catchPhrase()

# print(200_000_000_000)

# class People:
#     def __init__(self ,name , age) -> None:
#         self.name = name
#         self.age = age
#     def __str__(self) -> str:
#         return f'{self.name} {self.age}'
# class run:
#     def run(self):
#         print("Run")
# class Name:
#     def names(self):
#         print(self)
# class Robot:
#     def __init__(self, model) -> None:
#         self.model = model

#     def __str__(self) -> str:
#         return self.model

    



# class Human(People , run , Name , Robot):
#     def __init__(self, name, age , model) -> None:
#         People.__init__(self ,name  , age)
#         Robot.__init__(self , model)
#     def __str__(self) -> str:
#         return f'{self.name} {self.age} {self.model}'
        

# h = Human("Nurti" , 19 ,"T34")
# print(h)


class comp:
    _monitor = 1
    def __init__(self , _model , os) -> None:
        self._model = _model
        self.os = os
    def __str__(self) -> str:
        return(f"{self._model} {self.os}")
g= comp("hp" , "Windows")
print(g)

    