def family(name):
    """This function counts the number of descendants
    a person has within the 'tree' dictionary."""
    
    if name not in tree:
        return 0

    count = len(tree[name])

    for child in tree[name]:
        count += family(child)

    return count


n = int(input())

tree = {}

for i in range(n):
    parent, child = input().split()

    if parent not in tree:
        tree[parent] = []

    tree[parent].append(child)

name = input()

print(descendants(name))
