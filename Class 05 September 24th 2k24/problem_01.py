s=input("Enter the String: ")

count=0
newList=s.split()

for word in newList:
    if word.lower() == word.lower()[::-1]:
        count+=1

print(count)

