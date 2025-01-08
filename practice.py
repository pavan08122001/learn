def sel_srt(arr):

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j]>arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def qui_srt(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]

    left = [i for i in arr[1:] if i<=pivot]
    right = [i for i in arr[1:] if i>pivot]

    return qui_srt(right)+[pivot]+qui_srt(left)

print(sel_srt([7,3,9,7,2,90]))
print(qui_srt([7,3,9,7,2,90]))