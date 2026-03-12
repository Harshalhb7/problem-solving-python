arr = list(map(int,input().split()))
start = 0
end = len(arr) - 1
for i in arr:
    if (start<end):
        arr[start],arr[end] = arr[end],arr[start]
    start = start + 1
    end = end -1

print(arr)
