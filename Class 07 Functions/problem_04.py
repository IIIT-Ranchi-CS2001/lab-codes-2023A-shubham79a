str=input("Enter String: ")
elements=str.split(" ")

print(elements)

uppercase_letters = list(
    map(lambda s: s.upper(), filter(lambda s: s.isalpha(), elements))
)
squared_digits = list(
    map(lambda x: int(x)**2, filter(lambda s: s.isdigit(), elements))
)
alphaNumeric=list(
    (filter(lambda s: s.isalnum(), elements))
)

print(uppercase_letters)
print(squared_digits)
print(alphaNumeric)
