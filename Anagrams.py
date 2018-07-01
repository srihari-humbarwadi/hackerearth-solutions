alphabet = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
while t > 0:
    a = input()
    b = input()
    _counta = {}
    _countb = {}
    for ch in alphabet:
        _counta[ch] = 0
        _countb[ch] = 0
    for ch in a:
        _counta[ch] += 1
    for ch in b:
        _countb[ch] += 1
    res = 0
    for ch in alphabet:
        res += abs(_counta[ch] - _countb[ch])
    print(res)
    t -= 1
