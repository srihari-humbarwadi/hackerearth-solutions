n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr_sum = [arr[0] for x in range(n)]
for i in range(1, n):
    arr_sum[i] = arr_sum[i-1] + arr[i]

while q > 0:
    low, high = map(int, input().split())
    low -= 1
    high -= 1
    diff = high - low + 1
    if low == 0:
        sum = arr_sum[high]
    else:
        sum = arr_sum[high] - arr_sum[low - 1]
    print(int(sum / diff))
    q -= 1