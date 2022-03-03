# Solution first
s = 'anagram'
t = 'nagarat'
def anagram(s,t):
    n1 = len(s)
    n2 = len(t)
    l1 = [0]*26
    l2 = [0]*26
    if n1!=n2:
        print(False)
        return False
    for i in range(n1):
        l1[ord(s[i])-ord('a')] +=1
        l2[ord(t[i])-ord('a')] +=1

    if l1==l2:
        print(True)
        return  False
    else:
        print(False)
        return False

# anagram(s,t)

# Solution second
"""
By using sorting algorithms
"""
s = sorted(s)
t = sorted(t)
print(s)
if s==t:
    print(True)

else:
    print(False)