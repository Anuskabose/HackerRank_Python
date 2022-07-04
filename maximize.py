a,b = map(int, raw_input().strip().split(' '))
c = []
for i in range(a):
    l = map(int, raw_input().strip().split(' ')[1:])
    c.append(l)
    
v = len(c) - 1
output = 0
def max(c, v, u, b):
    global output
    if v < 0:
        if u > output:
            output = u
        return
    for i in c[v]:
        max(c, v-1, (u + i ** 2 % b) % b, b)
max(c, v, 0, b)
print(output)
