

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

s = input().strip()
k = int(input().strip())

index = months.index(s)+1
index += k

while index > 12:
    index -= 12

print(months[index-1])



