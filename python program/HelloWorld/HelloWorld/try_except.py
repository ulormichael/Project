
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("Invalid Input")
except ValueError:
    print("invalid input")
