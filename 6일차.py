a = int(input("첫 번째 과목의 점수를 입력하세요.:"))
b = int(input("두 번째 과목의 점수를 입력하세요.:"))
c = int(input("세 번째 과목의 점수를 입력하세요.:"))
d = (a + b + c) // 3
if d >= 50:
    print("평균 점수는" + str(d) + "점으로 합격입니다.")
else:
    print("평균 점수는" + str(d) + "점으로 불합격입니다.")

word = input("단어를 입력해주세요.:")
line = input("문장을 입력해주세요.:")
if word in line:
    print("단어가 있습니다.")
else:
    print("단어가 없습니다.")