n = int(input())
translator = {}

for _ in range(n):
    ru, en = input().split()
    translator[ru] = en

phrase = input().split()

for word in phrase:
    if word in translator:
        print(translator[word], end=" ")
    else:
        print(word, end=" ") 
