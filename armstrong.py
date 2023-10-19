x = input()
x = str(x)
sum_digits = 0
for digit in x:
    sum_digits = sum_digits + int(digit)**len(x)
    print(sum_digits)
if sum_digits == int(x):
    print("Число Армстронга")
else:
    print("НЕ является числом Армстронга")




for number in range(10, 10000):
    number_str = str(number)
    sum_digits = 0
    for digit in number_str:
        sum_digits += int(digit) ** len(number_str)
        #print(sum_digits)
    if sum_digits == number:
        print(number, " - число Армстронга")
