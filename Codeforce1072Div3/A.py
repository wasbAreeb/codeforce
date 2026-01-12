
# # A. Social Experiment -> Mathematical, Constructive, greedy problem with parity-based reasoning

# Read number of test cases
t = int(input())

min_r = []
for _ in range(t):
    n = int(input())
    
    # Apply the pattern
    if n < 4:
        min_r.append(n)
    else:
        if n % 2 == 0:
            min_r.append(0)
        else:
            min_r.append(1)
    
for i in min_r:
    print(i)    
    
