list = [25, 14, 27, 16, 21, 5]


def max(a):
    num = 0

    for i in range(len(a)):
        if a[i] > a[num]:
            num = i
    return num


print(max(list)+1)
