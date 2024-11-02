
myList1=[courseName for courseName in input().split()]
myList2=[courseCode for courseCode in input().split()]


newList=[]
for i in range(len(myList1)):
    newList.append(myList1[i]+":"+myList2[i])
print(newList)



