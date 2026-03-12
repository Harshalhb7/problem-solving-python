arr = list(map(int,input().split()))
first_val = arr[0]
current = 0
next = 1

for i in arr:
    if(next < len(arr)):
        arr[current] = arr[next]
    elif(next == len(arr)):
        arr[current] = first_val
    current = current + 1
    next = next + 1

print(arr)
