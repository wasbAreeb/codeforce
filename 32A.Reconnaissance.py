
# Reconnaissance

n, d = map(int, input().split())

soldier = list(map(int,input().split()))

ways = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            if abs(soldier[i] - soldier[j]) <= d:
                ways += 1

print(ways)

