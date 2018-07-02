def decode(s):
    n = len(s)
    str = list(s)
    str = str[::-1]
    indices = [int(x / 2) for x in range(n)]
    res = []
    for i, ch in enumerate(str):
        res.insert(indices[i], ch)
    return ''.join(res)


T = int(input())
for _ in range(T):
    s = input()

    out_ = decode(s)
    print (out_)