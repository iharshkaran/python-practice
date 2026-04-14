num1 = int(input("Enter first Number : "))
num2 = int(input("Enter Second Number : "))
num3 = int(input("Enter third Number : "))

if(num1>num2 and num1>num3):
    print("first number is greatest",num1)
elif(num2>num3 and num2>num3):
    print("Second number is greatest",num2)
else:
    print("third number is greatest",num3)