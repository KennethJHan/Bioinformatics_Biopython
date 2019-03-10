#090-1.py

def palindrome_checker(s):
    for i in range(0,len(s)//2):
        #print(s[i])
        #print(s[len(s)-1-i])
        if s[i] != s[len(s)-1-i]:
            return False
    return True

s1 = "ACACA"
s2 = "ATTCA"
print(palindrome_checker(s1))
print(palindrome_checker(s2))
