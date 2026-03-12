string = input("Enter the string: ")
vowels = "aeiouAEIOU"
n = len(string)
for i in range(n):
    for j in range(i,n):
        substring = string[i:j]
        vowel_count = 0
        for v in substring:
            if v in vowels:
                vowel_count += 1
        if vowel_count % 2 == 0:
            print(substring)
