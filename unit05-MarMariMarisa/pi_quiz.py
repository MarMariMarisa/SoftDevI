from itertools import count

def pi_tester():
    count = 0
    a = ""
    pi_input = None
    pi_100 = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    while count < 100:
        a = input("Pleae enter the decimals of pi up to 100 decimals one at a time: ")
        pi_input = str(pi_input) + str(a)
        if str(a) != str(pi_100[count]):
            break
        else:
            count += 1
    return count
def display_score(score):
    title = ""
    if score >= 0 and score <= 4:
        title = "Pi Neophyte"
    if score > 4 and score <=9:
        title = "PI Novice"
    if score > 9 and score <= 24:
        title = "PI Journeyman"
    if score > 24 and score <= 49:
        title = "PI Enthusiast"
    if score > 49 and score <= 96:
        title = "PI Connoisseur"
    if score > 96 and score <= 100:
        title = "PI Expert"
    if score > 100:
        title = "PI Imposter"
    print("With a score of", score,"you are a", title)
def main():
    score = pi_tester()
    display_score(score)

main()