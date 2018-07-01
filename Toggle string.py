str = list(input())
for i, ch in enumerate(str):
    x = ord(ch)
    if x >= 97 and x <= 122:
        x -= 32
    else:
        x += 32
    str[i] = chr(x)
print(''.join(str))
