mapping = ["", "", "abc", "def", "ghi", "jkl","mno","pqrs","tuv","wxyz"]
i = 0
output = ''
digit = 23
ans = []
def solve(digit,output,i,ans,mapping):
    if i==len(str(digit)):
        ans.append(output)
        return ''

    num = int(str(digit)[i])
    string = mapping[num]
    
    for aa in range(len(string)):
        output+=string[aa]
        solve(digit,output,i+1,ans,mapping)
        output = output[:-1]

    return ans
print(solve(digit,output,i,ans,mapping))
# print(ans)
