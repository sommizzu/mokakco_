class calculator:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


num1 = int(input("첫 번째 정수를 입력하세요 :"))
num2 = int(input("두 번째 정수를 입력하세요 :"))

num = calculator(num1, num2)

print(num1, "과 ", num2, "의", "덧셈 결과 : ", num.add())
print(num1, "과 ", num2, "의", "뺄셈 결과 : ", num.sub())
print(num1, "과 ", num2, "의", "곱셈 결과 : ", num.mul())
print(num1, "과 ", num2, "의", "나눗셈 결과 : ", num.div())
