arr =[1,1,2,2,2]

ans = []
k = 5
# arr = sorted(arr)

# def printing(arr,local,ans,start,k):
#     if k<=0:
#         if k==0:
#             ans.append(local)
#         return
    
#     for i in range(start,len(arr)):
#         if i>start and arr[i]==arr[i-1]:
#             continue
#         printing(arr,local+[arr[i]],ans,i+1,k-arr[i])



# printing(arr,[],ans,0,k)
# print(ans)

def sub_sequence(arr,ans,local,k,start):
    if k<=0:
        if k==0:
            ans.append(local)
        return

    for i in range(start,len(arr)):
        if i>start and arr[i]==arr[i-1]:
            continue

        if arr[i]>k:
            break

        sub_sequence(arr,ans,local+[arr[i]],k-arr[i],i+1)


sub_sequence(arr,ans,[],4,0)
print(ans)
