
# A. Translation Problem. Solved the A. Translation proble; Tag-> String and implementation problem. 

word1 = input().strip()
word2 = input().strip()

# def translatable(word):
#     rev = []
#     for i in word:
#         rev.insert(0,i)

#     rev_s = ""
#     for i in rev:
#         rev_s += i

#     return rev_s

# Below is better optimized way. Otherwise above is based on implementation. 
if word1 == word2[::-1]:   #sequence[start : end : step]
    print("YES")
else:
    print("NO")


