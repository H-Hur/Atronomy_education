sum = 0
for number in range (0, 10):
    sum = sum + number
    print(number,sum)
print(' ')

sum = 0
for number in range(0, 10, 2):
    number = number + number
    sum = sum + number
    print(number,sum)
print(' ')

sum = 0
for number in range (0, 10, 1):
    sum = sum + number
    print(number, sum)
    if(number >= 4): break
print(' ')

sum = 0
for number in range (0, 10, 1):
    sum = sum + number
    if(number >= 4): break
    print(number, sum)
print(' ')


