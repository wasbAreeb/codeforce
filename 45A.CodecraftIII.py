
import math

months = ["Januray", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

month = input().strip()
k = int(input().strip())

index = months.index(month)+1
index += k

while index >= 12:
    index /= 12

print(months[index])
