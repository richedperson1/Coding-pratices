arr = [3,4,4]


rank = 1
total = 0


def classTest(n: int, arr: list[int], k: int)-> int:
    dist = {}
    for i in arr:
        if i in dist:
            dist[i]+=1
        else:
            dist[i] = 1

    num = sorted(dist,reverse=True)
    total = 0
    for i in num:
        total += dist[i]
        if total >=k:
            return(i)
print(classTest(len(arr),arr,1))