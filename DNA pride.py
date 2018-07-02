t = int(input())
dna = {
    'A':'T',
    'C':'G',
    'T':'A',
    'G':'C'
}
for x in range(t):
    res = ''
    n = int(input())
    str = input()
    for ch in str:
        if ch in dna:
            res += dna[ch]
        else:
            res = 'Error RNA nucleobases found!'
            break
    print(res)