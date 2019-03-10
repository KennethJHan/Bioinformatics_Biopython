#019_after.py
try:
    with open("noname.txt",'r') as fr:
        read = fr.readlines()
        print(read)
except FileNotFoundError:
    print("파일이 없습니다.")
