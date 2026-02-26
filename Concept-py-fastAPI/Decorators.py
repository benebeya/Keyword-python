# decorator is just a finction that can change the behaviour of a method or other function 
#often used to add more functionality 



def my_decorator (func):
    def wrapper ():
        print(f"Runing {func.__name__}")
        func ()
        print("Complete")
    return wrapper    




#do_this = my_decorator(do_this)
@my_decorator
def do_this ():
    print("Doing this")
 
 
@my_decorator   
def do_that ():
    print("Doing that")
    
do_this()
do_that()