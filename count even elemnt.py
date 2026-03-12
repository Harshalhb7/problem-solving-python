arr = list(map(int,input().split()))
n = 0
for i in arr:
    if (i%2==0):
        n = n + 1

print(n)