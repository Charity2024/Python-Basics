# arithmetic operator, assignment opperator ,logical operator, comparison operator

num = 43  # first operand
num2 = 12  # second operand
# Arithmetic operator
print(f"The sum of {num} and {num2} is {num+num2}")  # addition operator
print(f"The difference of {num} and {num2} is {num-num2}")  # subtraction operator
print(f"The division of {num} and {num2} is {num/num2}")  # division operator
print(f"The multiplication of {num} and {num2} is {num*num2}")  # multiplication operator
print(f"The remainder of {num} and {num2} is {num % num2}")  # modulus operator
print(f"The exponent of {num} and {num2} is {num**num}")  # exponential operator
print(f"The floor of {num} and {num2} is {num//num}")  # exponential operator

# Comparison operator
num3 = 56
num4 = 23

print(f"{num3} and {num4} are equals: {num3 == num4}")
print(f"{num3} and {num4} are not equals:{num3 != num4}")
print(f"{num3} is greater than {num4}: {num3 > num4}")
print(f"{num3} is less than {num4}:{num3 < num4}")
print(f"{num3} is less than or equal to {num4}:{num3 <= num4}")
print(f"{num3} is greater than or equal to {num4}:{num3 >= num4}")


# assignment operators
num5 = 27
num6 = 8

print(f"num5=num6: {num5 == num6} ")
print(f"num5 +=num6: {num5 + num6} ")
print(f"num5 -=num6: {num5 - num6} ")
print(f"num5 *=num6: {num5 * num6} ")
print(f"num5=num6: {num5 / num6} ")


# Logical operator

num7 = 10
print(f"one statement is true: {num7 >=15 or num7 < 12}")
print(f"one statement is true :{num7 >=15 and num7 < 12}")
