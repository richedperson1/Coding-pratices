from collections import deque
q = deque()



string = "askdsjfkasdkjfhajscdnjkndjk"
def manupulate(string):
    form = ''
    dist = {}
    for char in string:
        if char in dist:
            dist[char]+=1
        else:
            dist[char]=1
        q.append(char)
        while len(q)>0:
            if dist[q[0]]>1:
                q.popleft()
            else:
                form+=q[0]
                break 
        if len(q)==0:
            form+='#'
    return(form)
print(manupulate(string))