t = int(input("키를 입력하세요.:"))
w = int(input("몸무게를 입력하세요.:"))
bmi = w / (t / 100)** 2
if bmi >= 25:
    print("비만입니다")
elif bmi >= 23:
    print("과체중입니다")
elif bmi >= 18.5:
    print("정상체중입니다.")
else:
    print("저체중입니다")