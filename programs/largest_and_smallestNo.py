numbers = [45, 12, 89, 34, 67, 23, 91, 10]
largest = numbers[0]
smallest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number
print("Numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
