n = int(input())

dictionary = {}

for i in range(n):
    line = input().split()
    form = line[0]

    for item in line[1:]:
        dictionary[item] = form

check = input()

print(dictionary[check])
    
