arr = [2,3,4,2]
# This method is work when only two time one number is repeated

xor_of_array = arr[0]
for idx,data in enumerate(arr):
    if idx==0:
        continue
    
    xor_of_array^=data

for i in range(1,len(arr)):
    xor_of_array^=i

print(xor_of_array)
# print(1^0)


# method 2 
# This method work at every case 
# [2,2,2,2] is also work
set_of_array = set()
for data in arr:
    if data in set_of_array:
        print(data)
        break
    else:
        set_of_array.add(data)
