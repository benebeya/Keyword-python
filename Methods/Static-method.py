class Employee :
    def __init__(self, name , position):
        self.name = name 
        self.position = position 
   #instance  method each object that we create will have this method     
    def get_info (self):
        
        return f"{self.name} = {self.position}"
   # this is static method it belong to the class not any obj created from that class
   #Usually used for general utility function that do not need to class data  
    @staticmethod
    def is_valide_position (position ):
        valid_position = ["Manager","Cashier","Cook","janitor"]
        return position in valid_position
    
    
print(Employee.is_valide_position("Rocket scientest "))
employee1 = Employee("jhon", "Manager")
employee2 = Employee("david", "Janitor")
employee3 = Employee("Spongbob", "Cook")

print(employee1.get_info())
