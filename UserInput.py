print("""
Choose a num from [1 to 4]
      1 for Addition
      2 for Subtraction
      3 for Multiplication
      4 for Division """)
num = int(input("Enter your num: "))

a = int(input("Enter your First Number: "))
b = int(input("Enter your Second Number: "))

if num == 1:
    print(f"The sum of {a} + {b} = {a+b}")

elif num == 2:
    print(f"The Difference of {a} - {b} = {a-b}")

elif num == 3:
    print(f"The Product of {a} * {b} = {a*b}")

elif num == 4:
    print(f"The Quotient of {a} ÷ {b} = {a/b}")

else:
    print("Enter a valid number !")
