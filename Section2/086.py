#086.py

class MyClass:
    def __init__(self):
        self.seq = ""
        
    def __gt__(self, other):
        if len(self.seq) > len(other.seq):
            return("%s is longer than %s." %(self.seq, other.seq))
        elif len(self.seq) < len(other.seq):
            return("%s is not longer than %s." %(self.seq, other.seq))
        else:
            return("The length is same.")

obj1 = MyClass()
obj2 = MyClass()
obj3 = MyClass()
obj4 = MyClass()

obj1.seq = "AAAA"
obj2.seq = "TTT"
obj3.seq = "GGG"
obj4.seq = "CC"

print(obj1 > obj2)
print(obj2 > obj3)
print(obj4 > obj3)
