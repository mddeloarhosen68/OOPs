a = 5
b = 2

try:
    print("Resource Open")
    print(a / b)
    k = int(input("Enter The Number: "))
    print(k)


except ZeroDivisionError as e:
    print("Hey,You Cannot divide a number by Zero")

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something is wrong.")

finally:
    print("Resource Close")
