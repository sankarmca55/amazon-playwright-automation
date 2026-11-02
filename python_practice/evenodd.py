#Print even and Odd numbers in a given range

#number = int(input("Please enter a number: "))

for number in range(1, 11):
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")

