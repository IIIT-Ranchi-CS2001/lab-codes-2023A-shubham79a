import math
a=int(input("First number "))
b=int(input("second number "))
c=int(input("third number "))

d=(b**2)-(4*a*c)


if d==0:
    ans=(-b)/(2*a)
    print(ans)
elif d>0:
    ans=(-b+(math.sqrt(d))/(2*a))
    print(ans)
else:
    real_root=(-b)/(2*a)
    complex_root=(math.sqrt(-d)/(2*a))
    ans=complex(real_root,complex_root)
    print(ans)


