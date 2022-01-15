import re
from tabnanny import check
patten = '[^a-zA-Z0-9]'


def checkPalindrome(s):
    # Write your code here
    # Return a boolean
    n = len(s)
    j = n-1
    i = 0
    while i<n and j >=0:
        while j>=0 and (j == ' ' or bool(re.search(patten, s[j]))):
            j -= 1

        while i<n-1 and( i == ' ' or bool(re.search(patten, s[i]))):
            i+=1
        if s[i].lower() != s[j].lower():
            return 'No'
        j -= 1
        i+=1
    return 'Yes'


print(checkPalindrome('+3m$M3? =+@-?? +$-$'))
