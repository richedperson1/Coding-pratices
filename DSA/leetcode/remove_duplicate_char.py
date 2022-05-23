
# ----------------------------------------------| method 1 |---------------------------------------------------------#

string = "aabbcced"
k = 3

stack = []
count = []
last_char_count = 0


ind = 0

for word in string:
    if stack and stack[-1][0] == word:
        stack[-1][1] += 1
    else:
        stack.append([word, 1])

    if stack[-1][1] == k:
        stack.pop()

res = ""
for word, co in stack:
    res += (word*co)
print(res)
