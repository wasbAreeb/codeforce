
# 16/01/2026. It took me two days to understand this problem clearly. Solved it on 17/01/2026
# This problem was designed for Kotlin Heroes programming language. It was not available for other language. 
# I used website to convert python code to kotlin. Logic matters. So my logic applied correct and submission happened successfully in first attempt.

tests = int(input().strip())

test_impossible = []
test_impossible_model = []

for i in range(tests):
    n = (int(input().strip()))
    model = list(map(int, input().split()))

    min_model = model[0]
    impossible = 0
    impossible_model = []

    for i in range(n):
        if i == 0: continue

        if model[i] <= min_model: min_model = model[i]
        else: impossible += 1; impossible_model.append(i+1)

    test_impossible.append(impossible)
    test_impossible_model.append(impossible_model)


for i in range(tests):
    print(test_impossible[i])
    for j in test_impossible_model[i]:
        print(j, end=" ")    
    print()

