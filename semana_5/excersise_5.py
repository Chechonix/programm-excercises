numbers = []     
counter = 0

while counter < 10:
    num = int(input("Enter your number: "))
    numbers.append(num)
    counter += 1

highest = numbers[0]
for n in numbers:
    if n > highest:
        highest = n

print(numbers)
print("The highest number was", highest)
