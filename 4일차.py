a = 3420
b = a // 1000
c = a % 1000
print("1000원 : %d개" % b)

de = c // 100
e = c % 100
print("100원 : %d개" % de)

f = e // 10
print("10원 : %d개" % f)

g = (de + f)
print("필요한 동전의 개수 :%d개" %g)