
def build_table1(rows, cols):
    table = []
    for r in range(rows):
        row = []
        for c in range(cols):    
            row.append(10*r+c)
        table.append(row)
    return table

def build_table2(rows, cols):
    return [[(10*r+c) for c in range(cols)] for r in range(rows)]


def main():
    table1 = build_table1(4, 6)
    table2 = build_table2(4, 6)
    print("table1 = ", table1)
    print("table2 = ", table2)
    assert table1 == table2

main()


