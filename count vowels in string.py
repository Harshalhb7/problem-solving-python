string = input("Enter the string: ")
arr = list(string)
count = 0
vowel = ['a','e','i','o','u','A','E','I','O','U']
for i in arr:
    if i in vowel:
        count = count + 1
print("No. Of Vowels: ",count)
