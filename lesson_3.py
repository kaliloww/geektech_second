# Тема инкапсуляция
# инкапсуляция закдючение в одного место (класс) для работы с ним 

# публичная защита
class Human:
    atribute = 1
    def __init__(self , name , age) :
        self.name = name
        self.age = age 
    def __str__(self) -> str:
        return f"name is {self.name}\n"\
            f"age is {self.age}"
    def run(self):
        print(f"{self.name} is run")

h= Human("Nurtilek" , 19 )
print(h)



