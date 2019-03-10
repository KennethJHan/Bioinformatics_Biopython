#085.py

class MyClass:
    def __init__(self):
        self.seq = ""
        
    def __add__(self, other):
        return self.seq + other.seq

obj1 = MyClass()
obj2 = MyClass()

obj1.seq = "AAA"
obj2.seq = "TTT"

print(obj1 + obj2)

