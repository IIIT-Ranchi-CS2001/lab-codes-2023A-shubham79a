S="Ba Ba Black Sheep"

# 2) a.
print(len(S))

# 2) b.

# for num in range(0,len(S)):
#     if S[num]=="e":
#         print(num)
#         break

print(S.index("e"))


# 2) c.

# count=0
# for num in range(0,len(S)):
#     if S[num]=="a":
#         count+=1
# print(count)

print(S.count("a"))

# 2) d.
myString=S.split()
s="Ta Ta "+myString[2]+" "+myString[3]
print(s)

