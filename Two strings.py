t = int(input())
while t > 0:
    str1, str2 = map(list, input().split())
    if ''.join(sorted(str1)) == ''.join(sorted(str2)):
        print('YES')
    else:
        print('NO')
    t -= 1