# While Loop
num = 10
while num > 0:
    print(num)
    num -= 1

# break
num = 10
while num > 0:
    if (num == 5):
        break
    print(num)
    num -= 1

# continue
num = 10
while num > 0:
    num -= 1
    if (num == 5):
        continue
    print(num)
