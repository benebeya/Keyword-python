"""import asyncio
from asyncio import Future
async def my_task(nbre:int ) ->dict :
    print("Starting task...")
    await asyncio.sleep(2)
    return{"task":nbre}

async def main ()->None :
    tasks:Future =asyncio.gather(my_task(1),my_task(2), my_task(3))
    result :list[dict] = await tasks 
    print(result)
    
if __name__=="__main__":
    asyncio.run(main())"""
#9.break------------------------------------------------------------------
"""for i in range(10):
    if i == 5:
        break
    else:
        print (i)
print ("after break the program will stop ")
"""
#10.class -----------------------------------------------------------------------
"""class Person:
    def __init__(self, name :str)-> None :
        self.name = name 
        
    def work (self )->None:
        print (f'{self.name} is working.')
p = Person("Ali")
p.work()"""
#11.continue -----------------------------------------------------------------
"""names :list[str] = ["Tom","Bob","james"]

for name in names :
    if name == "Bob":
        print("we do not say hello to Bob")
        continue
    print(f"hello, {name}!")"""
#12.def ----------------------------------------------------------------
"""def hello() :
   return "hello world"
x = hello()
print(x)"""
#13.del ------------------------------------------------------------------
"""age :int = 10
print (age)
del age
print(age)"""
#14 and 15 and 21.elif&else&if  -----------------------------------------------------------
"""weather :str = "sunny"
if weather == "rainy":
    print("Remember to bring an Umbrella!")
elif weather =="cloudy":
    print ("Remember to wear CloudCream!")
elif weather =="sunny":
    print("Rememeber to eat iceCream!")
else :
    print("IDK , not sure about the weather ")"""
#!16 and 17.except&finally -----------------------------------------------------------
"""from typing import Never 

def dangerous_code()-> Never:
    raise ValueError("Bad value")
try:
    dangerous_code()
except ValueError as e :
    print(f"Yoo, you messed up: {e}")
finally:
    print("finally: I run no matter what happens")"""
#18 and 19 and 22.for&from&import --------------------------------------------------------------
"""from random import randint 

for i in range (4):
    print (randint(10,20))"""
#20.global-------------------------------------------------------------------
"""name : str = "Bob"
def change_name():
    global name 
    name = "james"#now refers to the global var 

change_name()
print(name )"""
#23.is : compare the memory address --------------------------------------------------------------
"""class Fruit:
    ...

apple:Fruit = Fruit()
other_apple = apple
print(apple is other_apple)
print(f"{id(apple)=}")
print(f"{id(other_apple)=}")"""
#24lambda---------------------------------------------------------------------
"""def add(x:int  , y:int  ) -> int:
    return x + y 
result = add(7,2)
print (result )#<->
(lambda x,y :print(x+y) )(7,2)"""
#25nonlocal--------------------------------------------------------------
"""def func()-> None :
    item:str = "botle of water"
    def inner_func()-> None :
        nonlocal item
        print(item)

    inner_func()    
func()"""
#26. not --------------------------------------------------------
"""selected_user :str | None = None 

if selected_user is not None:
    print (f"you have selected :{selected_user}")
else:
    print(f"No user selected ....")"""
#27.or -------------------------------------------------------------------
"""a,b,c = 5,10,20
if c > a or  a == b :
    print ("One of the coditions were sarisfied ")"""
#30.raise -----------------------------------------------------------
"""raise Exception("Manually raised an exception for no reason .")"""
#32.try ---------------------------------------------------------
"""try:
    result = 100/0
except ZeroDivisionError:
    print ("GO home Bob you\'re drunk .....")"""
#33.while -------------------------------------------------------------------
"""import time

is_connected:bool = True 
i:int = 1
while is_connected:
    if i == 3:
        is_connected= False
    print(f"onnected for :{i}s")
    time.sleep(1)
    i= i +1
print("Connection lost....")"""
#34.with(context manager )---------------------------------------------------------
"""import threading

lock = threading.Lock()

with lock:
    print("critical section")"""
#?35.yield (create generators )--------------------------------------------------------
from typing import Generator

def generate_numbers(limit :int )-> Generator:
    for i in range (0, limit):
        yield i 

numbers : Generator =  generate_numbers(limit=10)
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(list(numbers))

#todo:softKeywords1.case and match--------------------------------------------------------

"""def describe_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"
print(describe_status(404)) """
