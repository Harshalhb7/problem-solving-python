string =  input("enter the string: ")
arr = list(string)
aplha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in arr:
    if i in aplha:
        continue
    else:
        print("failed")
        break
else:
    print("success")