n = int(input())
t = 'hackerearth'
s = input()
count = {}
count['h'] = 0
count['a'] = 0
count['e'] = 0
count['r'] = 0
for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1
result = count['h']
count['h'] /= 2
count['a'] /= 2
count['e'] /= 2
count['r'] /= 2

for ch in t:
    if ch in count:
        if result > count[ch]:
            result = count[ch]
print(int(result))