arr = list(map(int, ('55 52 33 100 77 61 40 69').split()))
lst = []
# local =[]
for data in range(0, len(arr), 2):
    local = []
    local.append(arr[data])
    local.append(arr[data+1])
    lst.append(local)

petrol = lst
print(petrol)
n = len(petrol)
balance = 0
exost = 0
start = 0
for i in range(n):
    balance += (petrol[i][0]-petrol[i][1])
    if balance<0:
        exost+=balance
        balance = 0
        start = i+1

if balance+exost>=0:
    print(start)
else:
    print(-1)