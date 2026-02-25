
from abc import ABC , abstractmethod

class Vechicle(ABC) :
    
    @abstractmethod
    def go (self):
        pass
    
    @abstractmethod
    def stop (self):
        pass
    
    
class Car (Vechicle):
       
    def go (self):
        print("you drive the car ")
        
    def stop(self):
        print("you stop the car ")

class Motorcycle(Vechicle):
    
    def go (self):
        print("you ride  the motorcycle ")
        
    def stop(self):
        print("you stop the motorcycle ")

class Boat(Vechicle):
       
    def go (self):
        print("you sail the boat")
    def stop(self):
        print("you anchor the boat") 
        
   
boat =Boat()
boat.go()
boat.stop()