import math as m

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
x = float(input('x='))

if x < 0 and b != 0:
    print(x**(1/3))
    print((m.cbrt(x) + b) / a)
elif x > 0 and b > 0:
    print((x**2 - m.sin(a-2))/(3 * x - b*c))
else:
    print(m.log(x)/c)
