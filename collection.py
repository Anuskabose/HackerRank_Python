from collections import Counter

s = int(input())
sizes = Counter(map(int,raw_input().split()))
A= int(input())
earnings = 0

for i in xrange(A):
    size,s = map(int,raw_input().split())
    if sizes[size]>0:
        sizes[size]-=1
        earnings += s
        
print earnings
