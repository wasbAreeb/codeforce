
n = int(input().strip())

soldier = list(map(int,input().split()))

min_height_diff = float('inf')  #A very large number stored in the system
min_i = 0
min_j = 0

for i in range(n):
    # if i < n - 1: 
    #     j = i + 1
    # else: 
    #     j = 0   You can do this by using mathematical logic

    j = (i + 1) % n
        
    diff = abs(soldier[i] - soldier[j])

    if diff < min_height_diff:
        min_height_diff = diff
        min_i = i
        min_j = j
        
print(min_i+1, min_j+1)

