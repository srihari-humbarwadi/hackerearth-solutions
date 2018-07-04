a = input()
b = input()
count = 0
if sorted(a) != sorted(b):
    print('-1')
else:
    for i, x in enumerate(a):
        if a[i] != b[i]:
            count += 1;
    print(int(count / 2))