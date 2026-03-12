arr = list(map(int,input().split()))
largest  = 0
sec_larg = 0
for i in arr:
    if ( i > largest):
        sec_larg= largest
        largest = i

    elif i > sec_larg and i > largest:
            sec_larg = i
print(sec_larg)