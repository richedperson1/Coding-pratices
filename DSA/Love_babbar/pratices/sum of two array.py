def sumi(a, b, n, m):
    form = []
    carry = 0
    n -= 1
    m -= 1
    while m >= 0 and n >= 0:
        local_s = a[n]+b[m]+carry
        if local_s <= 9:
            form.append(local_s)
            carry = 0
            n -= 1
            m -= 1
        else:
            form.append(local_s % 10)
            carry = local_s//10
            n -= 1
            m -= 1

    while n >= 0:
        local_ss = a[n]+carry
        if local_ss <= 9:
            form.append(a[n]+carry)
            carry = 0
            n -= 1
        else:
            local = local_ss % 10
            form.append(local)
            carry = local//10
            n -= 1

    if n <= -1 and carry > 0:
        form.append(carry)

    return form[::-1]


a = {"tuv":256,"jaisw":26}
print(a.keys())

print([2*n for n in range(5)])