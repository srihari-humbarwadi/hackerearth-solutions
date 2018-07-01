n = int(input())
arr = list(map(int, input().split()))
print(sum(arr[0::3]), sum(arr[1::3]), sum(arr[2::3]))