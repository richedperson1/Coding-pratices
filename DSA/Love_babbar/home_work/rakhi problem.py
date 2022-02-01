"""
Ninja is celebrating Raksha Bandhan with his ‘N’ sisters. Each of his sisters plans to tie him one Rakhi, having some integer value. The integer value for all ‘N’ Rakhis is provided in an array ‘ARR’.
Ninja wants the total sum of values of all tied Rakhis to be strictly positive.
Your task is to tell him the maximum Rakhis he can have on his hand.

"""


def rakshaBandhan(arr: list[int], n: int) -> int:
    sumi = 0
    total = 0
    arr = sorted(arr)
    for i in range(n-1, -1, -1):
        if total+arr[i] > 0:
            sumi += 1
            total += arr[i]
    return sumi


arr = list(map(int, ('7 15 11 14 8 -6 -3 -20 -13 19 -12 2 -15 -9 -12 -15').split()))
# print(rakshaBandhan(arr,len(arr)))
