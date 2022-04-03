"""
Time complexity : O(n)
space complexity : O(1)
"""


num = 2.100
power = 2
def divide_and_conquer(num,power):
    if power==1:
        return num

    else:
        mid = power//2
        ans = divide_and_conquer(num,mid)
        c = ans*ans        # Smart move to calculate tree output
        if power&1==1:
            return c*num
        else:
            return c

def power_unit(num,power):
    if power==0:
        return 1
    elif power>0:
        return divide_and_conquer(num,power)

    else:
        return 1/divide_and_conquer(num,abs(power))

print(power_unit(num,power))