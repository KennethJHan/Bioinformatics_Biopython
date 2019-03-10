#083.py

class MyClass:
    def __init__(self):
        print("object created!")
        self.seq = ""
    
    def get_length(self):
        return len(self.seq)

obj = MyClass()
obj.seq = "ACGTACGT"
print(obj.get_length())

