"""first method"""


inputs = str(input("enter no. or name: "))
outputs = inputs[::-1]      # its use for reverse string
if inputs == outputs:
    print(inputs, "is palindrome")
else:
    print(inputs, "is not palindrome")



"""second method"""


inputs = str(input("enter no. or name: "))
outputs = "".join(reversed(inputs))      # reverse the input & join
if inputs == outputs:
    print(inputs, "is palindrome")
else:
    print(inputs, "is not palindrome")




"""3rd method using for loop"""


inputs = str(input("enter no. or name: "))
outputs = ""
for i in inputs:
    outputs = outputs.join(reversed(inputs))       # reverse the input & join
    if outputs == inputs:
        print(inputs, "is palindrome")
    else:
        print(inputs, "is not palindrome")
    break
