n = int(input())
arr = list(map(int, input().split()))
arr = arr[::-1]
arr.sort()
arr = arr[::-1]
sum = arr[0]
res = 1
for i in range(1, n):
    if sum + arr[i] >= sum:
        sum += arr[i]
        res += 1
    else:
        continue
print(sum, res)
