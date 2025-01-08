arr=['b','c','d','f']
count=ord(arr[0])
for i in range(len(arr)):
    if arr[i]==chr(count):
        count+=1
    else:
        print(chr(count))
        break