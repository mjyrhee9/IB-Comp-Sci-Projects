import random
sales = [[random.randint(0,100)for col in range(7)]for row in range(10)]
print (sales)
def salespractice (matrix, start_row, start_col, end_row, end_col):
    first_total = 0
    in_total=0
    last_total=0
    fee = [2,10]

    for col in range(start_col,7):
        if col < 5:
            first_total = first_total + matrix[start_row][col] * fee(0)
        else:
            first_total = first_total + matrix[start_row][col] * fee(1)

    for row in range (start_col + 1 , end_row):
        for col in range(7):
            print(matrix[row][col])
