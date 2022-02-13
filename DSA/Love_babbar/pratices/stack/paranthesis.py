string = '[(])'


def valid(string):
    stack = []
    close = {'}':'{',']':'[',')':'('}
    for para in string:
        if not stack:
            stack.append(para)

        else:
            if para in close:
                if stack[-1]==close[para]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(para)

    if not stack:
        return True
    else:
        return False

print(valid(string))