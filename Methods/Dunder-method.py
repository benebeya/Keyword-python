# Dunder methods (double underscore)__init__,__str__, __eq__
#they are automatically called by many of python built-in operation 
#!they allow developers to define or customize the behavior of an objects


class Book:
    
    def __init__(self, title , author , nbre_pages):
        self.title = title
        self.author = author
        self.num_page = nbre_pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, Other):
        return self.title == Other.title and self.author == Other.author 
    
    
    def  __lt__(self, other) :
        return self.num_page < other.num_page
    
    def  __gt__(self, other) :
        return self.num_page > other.num_page
    
    def __add__(self, other):
        return f"{self.num_page + other.num_page} pages"
    
    def __contains__(self, Keyword):
        return Keyword in self.title or Keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_page":
            return self.num_page
        else:
            return f"Key '{key}' was not found "
        
book1 = Book("the hobbit", "J.R.R. Tolkien", 310)
book2 = Book("A", "B", 223)
book3 = Book("A", "B", 172)


print(book2 < book3 )
print(book2 > book3)
print(book2 + book3)
print("hobbit" in book1)
print(book1["audio"])

