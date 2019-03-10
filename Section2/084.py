#084.py

class MyClass:
    def __init__(self):
        print("object created!")
        self.seq = ""
        
    def __del__(self):
        print("object deleted!")
    
    def get_length(self):
        return len(self.seq)

obj = MyClass()
del obj

