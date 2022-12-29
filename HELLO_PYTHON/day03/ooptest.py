class Animal:
    def __init__(self) :
        # print("생성자")
        self.age = 0

    def getOlder(self):
        self.age += 1   
        
    # def __del__(self):
    #     print("소멸자")
            
class Human(Animal) :
    def __init__(self):
        super().__init__()
        self.language = 0 

    def momstouch(self, stroke):
        self.language += stroke

# if __name__ == '__main__':    
#     ani = Animal()
#     print(ani.age)
#     ani.getOlder()
#     print(ani.age)

if __name__ == '__main__':
    hum = Human()
    print(hum.language)
    print(hum.age)
    hum.getOlder()
    hum.momstouch(5)
    print(hum.language)
    print(hum.age)