num = []

for i in range(7):
    num.append(int(input("정수를 입력하세요.: ")))

sum = 0
for i in num:
    sum += i

print("평균: ", sum/7)
