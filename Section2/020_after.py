#020_after.py
try:
    num = int(input("Enter: "))
    print(10 / num)
except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")
except ValueError:
    print("값을 입력해주세요.")
