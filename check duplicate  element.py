arr = list(map(int,input().split()))
for i in arr:
    for j in arr:
        if arr[i] == arr[j]:
            print("duplicate")
            