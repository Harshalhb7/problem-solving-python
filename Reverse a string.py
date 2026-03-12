string = input("Enter the string: ")
arr = list(string)
start = 0
end = len(arr) - 1
while start < end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
print("".join(arr))
