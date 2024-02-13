# example one
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

answer = num1 + num2 + num3

print(f"The sum of {num1}, {num2} and {num3} is: ", answer)


# example two
weight = float(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight // 0.45
    print("Weight in Lbs:" + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kg: " + str(converted))
