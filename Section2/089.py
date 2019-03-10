#089.py

def mer(n, arr1, arr2):
    if n == 1:
        return arr2
    else:
        tmp = []
        for i in arr1:
            for j in arr2:
                tmp.append(i+j)
        arr2 = tmp
        n -= 1
        return mer(n, arr1, arr2)
    
    
arr1 = ["A", "C", "G", "T"]
arr2 = ["A", "C", "G", "T"]
print(mer(3, arr1, arr2))
