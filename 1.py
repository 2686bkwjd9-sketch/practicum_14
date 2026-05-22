words = input().split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word in sorted_words:
    print(word[0])
