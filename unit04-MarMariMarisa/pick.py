import random
def is_correct(guess, answer):
    if guess == answer:
        return True
    return False

def main():
    answer = random.randint(1,10)
    guess = int(input("Please enter your first guess between 1 and 10 inclusive: "))
    is_correct(guess, answer)


main()

