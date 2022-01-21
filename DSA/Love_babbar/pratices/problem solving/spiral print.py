arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

start_row = 0
start_col = 0

row = len(arr)
col = len(arr[0])

total = row*col
end_row = row-1
end_col = col-1
count = 0
form = []
while len(form) < total:
    i = start_col
    while len(form) < total and i <= end_col:
        form.append(arr[start_row][i])
        i += 1

    start_row += 1
    i = start_row
    while len(form) < total and i <= end_row:
        form.append(arr[i][end_col])
        i += 1

    end_col -= 1

    i = end_col
    while len(form) < total and i >= start_col:
        form.append(arr[end_row][i])
        i-=1

    end_row -=1

    i = end_row
    while len(form) < total and i >=start_row:
        form.append(arr[i][start_col])
        i-=1
    
    start_col +=1
print(form)