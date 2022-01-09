num = int(input("정수를 입력하세요.:"))

def sum(n):

    x = 0
    for i in range(0, num + 1):
        x += i
    return x
print(sum(num))