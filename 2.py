n = int(input())
dict = {}

for i in range(n):
    ru, en = input().split()
    dict[ru] = en

phrase = input().split()

for word in phrase:
    if word in dict:
        print(dict[word], end=" ")
    else:
        print(word, end=" ") 
