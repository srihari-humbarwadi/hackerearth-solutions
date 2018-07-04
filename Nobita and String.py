t=int(input())
while t:
    t-=1
    strr = input().split(" ")
    newstrr = strr[::-1]
    print(' '.join([str(item) for item in newstrr]))