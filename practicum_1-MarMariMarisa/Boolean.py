def max_2(x, y):
    if x > y:
        return x
    elif y > x:
        return y
    if y == x:
        return x
def max_3(x,y,z):
    a = max_2(x,y)
    return max_2(a,z)
def grade(score1, score2):
    avg = (score1 + score2) / 2
    if avg >= 90 and (score1 and score2 >= 85):
        return "A"
    elif avg > 90:
        return "B"

    if 90 > avg >= 80 and (score1 and score2 >= 70):
        return "C"
    elif 90 > avg >= 80:
        return "D"
    
    if 80 >= avg >= 70 and (score1 and score2 >= 60):
        return "E"
    
    if 70 > avg or (score1 or score2 < 60):
        return "F"

def main():
    print(max_2(2,7))
    print(max_3(1,12,3))
    print(grade(90,92))
    print(grade(100,82))
    print(grade(72,90))
    print(grade(100,69))
    print(grade(100,50))


if __name__ == '__main__':
 main()