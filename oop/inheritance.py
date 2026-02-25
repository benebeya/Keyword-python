
# multiple and multilevel inheritance 

class Animal :
    
    def __init__(self, name ):
        self.name = name 
    
    
    def eat (self):
        print(f" {self.name} is eating ")
        
    def sleep (self):
        print(f" {self.name} is sleeping ")




class Prey (Animal):# فريسة
    def flee(self) :
        print(f" {self.name} is fleeing ")

class Predator (Animal): # مُفْتَرِس
    def hunt(self):
        print(f" {self.name} is Hunting")

class Rabbit (Prey): #أَرْنَب
    pass


class Hawk(Predator): #صَقْر 
    pass

class Fish(Prey, Predator): # سَمَكَة
    pass


rabbit =  Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

hawk.hunt()
fish.eat()
fish.flee()