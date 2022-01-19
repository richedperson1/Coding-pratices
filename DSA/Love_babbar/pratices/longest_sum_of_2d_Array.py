from re import L


def wavePrint(arr, row, col):

    # Write your code here.
    # Return a list of integers denoting the sine wave of the matrix
    form = []
    for i in range(col):
        if i & 1 == 0:
            for j in range(row):
                form.append(arr[i][j])
        else:
            for j in range(row-1, -1, -1):
                form.append(arr[i][j])
    return form
