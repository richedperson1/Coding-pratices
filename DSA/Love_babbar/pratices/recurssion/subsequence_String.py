def subset(arr,i,ans,output):
    if i>=len(arr):
        if output =='':
            return
        ans.append(output)
        return

    subset(arr,i+1,ans,output)
    
    subset(arr,i+1,ans,output+arr[i])


def making(arr):
    i = 0
    ans = []
    subset(arr,i,ans,'')
    return ans

print((making('bbb')))