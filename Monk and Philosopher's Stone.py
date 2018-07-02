class stack(object):
    def __init__(self):
        self.arr = []
        self.size = 0

    def push(self, data):
        self.arr.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        self.size -= 1
        data = self.arr[-1]
        del self.arr[-1]
        return data

    def getSize(self):
        return self.size

st = stack()
n = int(input())
arr = [int(x) for x in input().split()]
q, x = map(int, input().split())
for t in range(q):
    str = input()
    if str == 'Harry' and t < n:
        st.push(arr[t])
