max_number = int(input("Enter max number: "))

odd_numbers = []
for number in range(1, max_number):
    if number % 2 != 0:
        odd_numbers.append(number)
print("Create a list of all odd numbers between 1 and a max number. "
      + "Max number is something you need to take from a user using input() function\n", odd_numbers)