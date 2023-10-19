y = int(input())
'''int(y)
x = str(y)
sum_digits = 0
for digit in x:
    sum_digits = sum_digits + int(digit)**len(x)
    print(sum_digits)
if sum_digits == int(x):
    print("Число Армстронга")
else:
    print("НЕ является числом Армстронга")
'''
sum_digits = 1
num_digits=len(str(y))
print(y//10)
while (y // 10) > 0:
    sum_digits += (y % 10)**num_digits
    y = y // 10
print(sum_digits)


for number in range(10, 10000):
    number_str = str(number)
    sum_digits = 0
    for digit in number_str:
        sum_digits += int(digit) ** len(number_str)
        #print(sum_digits)
    if sum_digits == number:
        print(number, " - число Армстронга")
