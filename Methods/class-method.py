"""1. `Instance method` uses `self` and works with data of a specific object (instance variables).  
   2. `Class method` uses `cls` (`@classmethod`) and works with class-level data shared by all objects.  
   3. `Static method` uses no `self`/`cls` (`@staticmethod`) and is just a utility function inside the class."""
#Static method has no connections with the obj and is called by class name 
class Student :
    
    count = 0
    Total_gpa = 0
    def __init__(self, name , gpa ):
        self.name = name 
        self.gpa = gpa 
        Student.count += 1
        Student.Total_gpa += gpa
    #instance method 
    def get_info(self) -> int:
        return f"{self.name} {self.gpa}"
    # when we call the class method we can access or modify class data (count)
    #rather than self we use cls short for class  
    @classmethod
    def get_cont (cls):
        return f"Total number of students:{cls.count}"
    
    @classmethod
    def get_average_gpa(cls) -> float:
        if cls.count == 0 :
            return 0
        else:
            return f"Average gpa :{cls.Total_gpa/cls.count:.2f}"
    
    
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)
    
print(Student.get_cont())   
print(Student.get_average_gpa())