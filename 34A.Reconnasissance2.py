
n = int(input().strip())

soldier = list(map(int,input().split()))

min_height_diff = abs(soldier[1] - soldier[0])
min_i = 0
min_j = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        elif j < i:
            continue
        else:
            condition = abs(soldier[i] - soldier[j])
            if condition < min_height_diff:
                min_height_diff = condition
                min_i = i
                min_j = j

if min_i == min_j:
    print(1,2)
elif min_i != min_j:
    print(min_i+1, min_j+1)

