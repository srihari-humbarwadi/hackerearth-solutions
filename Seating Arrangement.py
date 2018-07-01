seats = ['WS', 'WS', 'MS', 'AS', 'AS', 'MS']
t = int(input())

# x = 5
while t > 0:
    x = int(input())
    q = int(x / 12)
    if x % 12 == 0:
        q -= 1
    sum = 12 * (2 * q + 1) + 1
    res = sum - x
    seat = res % 6
    print(res, seats[seat])
    t -= 1
