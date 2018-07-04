s = input().split()
res = ''
for i, str in enumerate(s):
    arr = list(str)
    if arr[0] >= 'a' and arr[0] <= 'z':
        arr[0] = chr(ord(arr[0]) - 32)
    if i != 0:
        res = res + ' ' + ''.join(arr)
    else:
        res = res + ''.join(arr)

print(res)