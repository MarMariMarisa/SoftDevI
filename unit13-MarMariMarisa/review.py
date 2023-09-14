def table(rows,cols):
    return [["(" + str(rows) + "," + str(col) + ")"] for col in range(cols)] for row in range(rows)]]

def main():
    a_table = table(5,7)
    for row in a_table:
        print(row)