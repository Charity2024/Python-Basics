num = int(input("Enter a number: "))

if num % 2 == 0:   # remainder operator
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

# example two

age = int(input("Enter age: "))
if age >= 18:
    print("You can vote")
else:
    print("You do not qualify to vote")
