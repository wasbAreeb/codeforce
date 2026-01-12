

def teams(n):
    teams = []

    if n < 0:
        return []
    if n == 2 or n == 3:
        teams.append(n)
        return teams
    if n % 2 == 0:
        teams = [2] * (n // 2)
    else:
        teams = [3] + [2] * ((n-3)//2)
    return teams
            

print(teams(7))
