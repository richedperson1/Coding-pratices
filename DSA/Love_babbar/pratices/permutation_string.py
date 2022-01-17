s1 = "eidczaooo"
s2 = 'azc'


def permutation(s1, s2):
    count1 = [0]*26

    for i in s2:
        index = ord(i)-ord('a')
        count1[index] += 1
    count2 = [0]*26
    i = 0
    n1 = len(s1)
    n2 = len(s2)
    k = len(s2)
    while i < n2:
        index = ord(s1[i])-ord('a')
        count2[index] += 1
        i += 1
    if count1 == count2:
        return("Ho gaya")
    while i < n1:
        index = ord(s1[i])-ord('a')
        count2[index] += 1
        index2 = ord(s1[i-k])-ord('a')
        count2[index2] -= 1
        i += 1
        if count1 == count2:
            return("HO gaya")
    return("Nai hoa")


print(permutation(s1, s2))
