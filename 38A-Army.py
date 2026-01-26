
# 1/25/2026. Successful submission in first attempt. Implementation Problem
n = int(input().strip())

rank = list(map(int, input().split()))

a,b = map(int,input().split())

years = 0
for i in range(a,b):
    years += rank[i-1]

print(years)

