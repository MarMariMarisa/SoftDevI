from decimal import DivisionByZero
from multiprocessing.sharedctypes import Value


def numbers():
    while True:
        filename = input("Please enter a file path: ")
        if filename == "":
            break
        try: 
            with open(filename) as file: # open raises a FIleNotFoundError
                sum = 0
                total_sum = 0
                for line in file:
                    try:
                        number  = float(line.strip()) # float() raises a Value Error
                        sum += number
                    except ValueError:
                        print("Skipping non numeric data:", line)
                print("Sum is:", sum)
                total_sum += sum
        except FileNotFoundError:
            print("File path", filename, "does not exist")

    print("The total sunm is", total_sum)

def password():
    pwd = input("Pleae enter a password between 10 and 20 characters: ")
    if len(pwd) < 10 or len(pwd) > 20:
        raise ValueError("Password length not valid")
    print("Valid!")

def divison():
    while True:
        errors = 0
        numerator = input("Please enter a numerator: ")
        denomenator = input("Please enter a denomenator: ")
        if numerator == "" or denomenator == "":
            break
        try:
            numerator = float(numerator) # raise value error
            denomenator = float(denomenator) # raise value error
            answer = numerator / denomenator # raise ZeroDivisionError
            print(numerator, "/", denomenator, "=",answer)
        except ValueError as ve:
            if errors < 3:
                print("Numeric data only")
            else:
                raise ve
            errors += 1
        except ZeroDivisionError as zde:
            if errors < 3:
                print("Cant divide by zero")
            else:
                raise zde
            errors += 1

def exponent(base, power):
        if power < 0:
            raise ValueError("Negative power!")
        product = 1
        for i in range(power):
            product *= base
        return product

def main():
    #numbers()
    # try:
    #     x = input("Enter a number: ")
    #     x = int(x)
    #     y = 2* x
    #     print("y =", y)
    # except:
    #     print("Invalid Input! Numeric data only!")
    # number = input("Enter your guess: ")
    # number = int(number)
    # if number < 1 or number > 10:
    #     raise ValueError("Number bewteen 1 and 10")
    # password()
    # divison()
    print("End of program")

main()