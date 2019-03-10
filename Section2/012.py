#012.py

def Factorial(num):
    result = 1
    
    while num > 0:
        result *= num
        num -= 1
    
    return result

num = 3
result = Factorial(num)
print(result)
