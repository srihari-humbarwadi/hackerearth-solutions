str = list('abcdefg')
n = len(str)
for i in range(n):
    for j in range(i, n):
        res = ''
        for k in range(i, j+1):
            res += str[k]
        print(res)