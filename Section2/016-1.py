#016-1.py
f = open("read_sample.txt",'r')
r = f.readlines()
f.close()
for s in r:
    print(s.strip())
