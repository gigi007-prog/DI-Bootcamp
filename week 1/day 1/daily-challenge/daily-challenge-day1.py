#1
string_text= input("Please enter a string")
if len(string_text)<10: 
    print("the string is too short")
elif len(string_text)>10:
    print("the string is too long")
elif len(string_text)==10:
    print("perfect sring")

print(string_text[0])
print(string_text[-1])

