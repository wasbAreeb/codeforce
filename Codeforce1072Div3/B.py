
# B. Hourglass Problem

# 17/01/2026: Understood 20% of the problem

t = int(input())

result = []
for _ in range(t):
    s, k, m = map(int, input().split())
    current_time = 0
    sand_finish_time = 0  # when current sand will finish (0 means no sand flowing)
    
    # Simulate up to time m
    while True:
        # Flip at current_time
        sand_finish_time = current_time + s
        # Next flip time
        next_flip = current_time + k
        
        if next_flip > m:
            # No more flips before m
            break
        else:
            current_time = next_flip
            # Continue loop to flip again
    
    # Now current_time is last flip time ≤ m
    # sand_finish_time is when current sand will finish
    
    if sand_finish_time > m:
        result.append(sand_finish_time - m)
    else:
        result.append(0)

for i in result:
    print(i)

