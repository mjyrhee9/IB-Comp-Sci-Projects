import random
sales=[[random.randint(0,100) for col in range(7)]for row in range(10)]
print(sales)

def salesCalculate(matrix,start_row,start_col,end_row,end_col):
    #get total for week a
    first_week_total=0
    inbetween_total=0
    last_week_total=0
    #fees for weekdays + weekends
    fee = [2,10]
    #get total for the start week
    for col in range(start_col,7):
        # if weekdays
        if col < 5:
            first_week_total = first_week_total + matrix[start_row][col] * fee[0]
        # if weekends

        else:
            first_week_total = first_week_total + matrix[start_row][col] * fee[1]
    print ('total for first week:', first_week_total)

    for row in range(start_row+1, end_row): #because of how python works no -1
        for col in range(7):
            print(matrix[row][col])
            if col < 5:
                inbetween_total = inbetween_total + matrix[row][col] * fee[0]
            else:
                inbetween_total = inbetween_total + matrix[row][col] * fee[1]
    print('total for inbetween', inbetween_total)

    for col in range(end_col,7):
        if col < 5:
            last_week_total = last_week_total + matrix[end_row][col] * fee[0]

        else:
            last_week_total = last_week_total + matrix[end_row][col] * fee[1]

    print ('total for last week:', last_week_total)

salesCalculate(sales,3,3,6,4)
