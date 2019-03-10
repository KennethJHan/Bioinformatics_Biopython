#090-2.py

def palindrome_checker(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
s1 = "ACACA"
s2 = "ATTCA"
print(palindrome_checker(s1))
print(palindrome_checker(s2))    
