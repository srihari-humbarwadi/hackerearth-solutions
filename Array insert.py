n, q = map(int, input().split())
arr = list(map(int, input().split()))
while q > 0:
    sum = 0
    x = list(map(int, input().split()))
    if x[0] == 1:
        arr[x[1]] = x[2]
    elif x[0] == 2:
        for i in range(x[1], x[2] + 1):
            sum += arr[i]
        print(sum)
    q -= 1