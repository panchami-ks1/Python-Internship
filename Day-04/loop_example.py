numbers = (1, 2, 3, 4)
sum = 0
for number in numbers:
    sum += number
# print("Sum is:", sum)

my_list = [1, 2, 3, 4, 5, 6, 7]
odd_sum = 0
even_sum = 0
for item in my_list:
    if item % 2 == 0:
        even_sum += item
    else:
        odd_sum += item

print("Odd sum is:", odd_sum)
print("Even sum is:", even_sum)
