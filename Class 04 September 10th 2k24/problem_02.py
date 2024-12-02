x=int(input("Enter the no.  whom you want to find the digit Sum: "))
y=x
ans=0
while x>0:
    ans+=int(x%10)
    x=x/10

print(f"Sum of digit of {y} is {ans}")