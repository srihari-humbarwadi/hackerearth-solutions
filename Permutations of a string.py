def permutation(string):
    permutations = []
    if len(string) == 1:
        return string
    for char in string:
        subpermutations = permutation(string.replace(char, ''))
        for subpermutation in subpermutations:
            result = char + subpermutation
            permutations.append(result)
    return set(permutations)


for perm in permutation(input()):
    print(perm, end=' ')
