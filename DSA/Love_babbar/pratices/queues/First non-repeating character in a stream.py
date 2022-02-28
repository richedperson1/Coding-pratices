arr = []
string = "askdjfkasdkjfhajscdnjkndjk"
form = ''
dist = {}
i = 0
for char in string:
    if char in dist:
        dist[char]+=1
    else:
        dist[char] = 1

    arr.append(char)
    while len(arr)>0:
        if dist[arr[0]]>1:
            arr = arr[1:]
        else:
            form+=arr[i]
            break
    if i==len(arr):
        form+='#'

print(form)
