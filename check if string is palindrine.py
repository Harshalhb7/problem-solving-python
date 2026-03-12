string = input("Enter a string: ")
arr = list(string)
start = 0
end = len(arr) - 1
while start < end:
    if arr[start] == arr[end]:
        start += 1
        end -= 1
    else:
        print("Not a palindrome")
        break
else:
    print("Palindrome")
