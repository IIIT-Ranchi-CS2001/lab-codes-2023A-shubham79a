str=input()

dict={}
#
for char in str:
    if char in dict:
        dict[char]+=1
    else:
        dict[char]=1

for char,count in dict.items():
    print(f"{char}:{count}")    
    
# if you want to skip spaces you can add condn 
# if you want to count lower a and upper A same then convert string to lowercase into different string
# s=str.lower() 