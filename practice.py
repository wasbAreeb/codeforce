
n = int(input())

round = []

for _ in range(n):
    name, score = input().split()
    score = int(score)
    round.append((name, score))

final_score = {}

for name, score in round:
    if name not in final_score:
        final_score[name] = score
    final_score[name] += score

max_score = max(final_score.values())

candidates = []

for name, total in final_score.items():
    if total == max_score:
        candidates.append(name)

current_score = {}
winner = None

for name, score in round:
    if name not in current_score:
        current_score[name] = score
    current_score[name] += score

    if name in candidates and current_score[name] >= max_score:
        winner = name
        break

print(winner)
