n = int(input())

dict = {}

for i in range(n):
    word1, word2 = input().split()
    dict[word1] = word2
    dict[word2] = word1

word = input()

if word in dict:
    print(dict[word])
else:
    print(word)
    
    
