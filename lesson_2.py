сс
print(g)
# g.run()
# Наслежование, полиморфизм  
#  инкапсуляция
# git
# class Human: #Суперкласс
#     head = 1
#     def __init__(self, name , age) -> None:
#         self.name = name
#         self.age=age
#     def __str__(self) -> str:
#         return f"name is {self.name}\n" \
#             f"age is {self.age}"
#     def run(self):
#         print(f'{self.name} is run')

# hum =Human("Sadir", 36)  #дочерний класс
# print(hum)
# class Student(Human): #Дочерний класс#2
#     head = 2
#     def __init__(self, name, age , lastname) -> None:
#         super().__init__(name, age)
#         Human.__init__(self , name , age)
#         self.lastname= lastname
#     def __str__(self) -> str:
#         return f"name is {self.name}\n" \
#             f"age is {self.age}\n"\
#             f"lastname is {self.lastname}"

# student = Student("Даниэль",60 , "Эрмеков")
# hum.run()
# student.run()

# print(f"{student} \n {student.head}")

# class teacher(Student):...

# tech = teacher("Beka",19,"DJU")
# print(tech)


# # class Robot:
# #     def noSleep(a):
# #         print(f'{a} funktion no Sleep True')

# # class Robot_2(Robot):...
# # Robot.noSleep(student.name)


