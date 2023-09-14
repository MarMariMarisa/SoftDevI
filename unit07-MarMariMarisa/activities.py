def evens(n):
    sum  = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += i
    return sum

def runner(a_func,n ):
    print(a_func.__name__)
    sum = a_func(n)
    print(sum)

def main():
    runner(evens, 10)


if __name__ == "__main__":
    main()