import re

exp = '((a/b))'


def findRedundantBrackets(arr):
    stack = []
    operator = ['+', '-', '*', '/']
    for char in arr:
        if char == '(' or char in operator:
            stack.append(char)

        else:
            if char == ")":
                redan = True
                while len(stack) > 0 and stack[-1] != "(":
                    if stack[-1] in operator:
                        redan = False
                    stack.pop()

                if redan:
                    return True
                stack.pop()

    if "(" in stack or ')' in stack:
        return True
    return False


print(findRedundantBrackets(exp))
