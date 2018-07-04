T = int(input())
for _ in range(T):
    sortedString = []
    str = list(input().strip())
    count = dict()
    revcount = dict()
    for ch in str:
            count.setdefault(ch, 0)
            count[ch] += 1
    for k, v in count.items():
        revcount.setdefault(v, [])
        revcount[v].append(k)
    sortedKeys = sorted(revcount.keys())
    for key in sortedKeys:
        revcount[key].sort()
        for ch in revcount[key]:
            sortedString.extend(ch * key)
    print(''.join(sortedString))