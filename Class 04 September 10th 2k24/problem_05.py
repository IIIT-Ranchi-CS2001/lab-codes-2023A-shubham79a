s=input()

# if s.isalnum():
#     print("True")
# else :
#     print("False")

for j in s:
    i=ord(j)
    # print(i)
    if(not(i>=65 and i<=90) and not(i>=97 and i<=122) and not(i>=48 and i<=57) ):
        print("False")
        break
else :
    print("True")
