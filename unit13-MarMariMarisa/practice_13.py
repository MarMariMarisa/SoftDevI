def recurse(limit,start = 3,integer_list = []):
    if start > limit:
        return integer_list
    else:
        if start % 3 == 0 and start % 5 != 0:
            hold = start
            start+=1
            integer_list.append(hold)
            return recurse(limit,start,integer_list)
        elif start % 5 == 0 and start % 3 != 0:
            hold = start
            start+=1
            integer_list.append(hold)
            return recurse(limit,start,integer_list)
        start+=1
        return recurse(limit,start,integer_list)

def main():
    list = recurse(20)
    print(list)


main()