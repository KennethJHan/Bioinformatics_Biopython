#088.py

arr = [0, 1]

def fibo(n):
    for i in range(n-1):
        arr.append(arr[-2] + arr[-1])
    return arr

print(fibo(10))



