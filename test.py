
arr = [2,3,4,6]
count = arr[0]
for i in range(len(arr)):
    if arr[i] == count:
        count+=1
    else:
        print(count)
        break
        