num = 0
for num in range(1, 101):
    if (num % 2 == 0 and num % 7 != 0):
        print(num)

result = 0

sum = 0
while True:
    number = int(input("숫자를 입력하세요:"))
    if number != 0:
        sum += number
    if number == 0:
        break
print(sum)