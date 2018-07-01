n = int(input())
a = list(map(int, input().split()))
res = 1
for x in a:
    res = (res * x) % 1000000007
print(res)