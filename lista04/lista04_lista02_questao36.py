from math import sqrt
a, b, c = map(float, input().split())
delta = b*b -4*a*c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + sqrt(delta)) / (2*a)
    r2 = (-b - sqrt(delta)) / (2*a)
    print('R1 = {0:.5f}'.format(r1))
    print('R2 = {0:.5f}'.format(r2))
