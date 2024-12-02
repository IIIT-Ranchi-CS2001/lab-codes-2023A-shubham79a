numbers=[int(x) for x in input("enter no. seprated by spaces : ").split()]
print(numbers)

n=len(numbers)

mean=sum(numbers)/n
numbers.sort()
if n%2==0:
    median=(numbers[n//2]+numbers[(n//2)-1])/2
else:
    median=numbers[n/2]


frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

max_count = max(frequency.values())
mode = [num for num, count in frequency.items() if count == max_count]

print(f"mean is {mean}")
print(f"median is {median}")
print(f"mode is {mode}")

