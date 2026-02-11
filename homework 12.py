#1
while True:
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        result = (a) / (b)
        print("result is ",result)
        break
    except ZeroDivisionError:
        print("You can't divide by zero")
    except ValueError:
        print("There is Value Error")
    except:
        print("Unexpected error")
#2
def calculate(a,b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "u can't divide by zero"
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result2 = calculate(a,b)
    print(result2)
except ValueError:
    print("There is ValueError")
#3
n = [1,2,3,4,5,6,7,8,9,10]
try:
    m = int(input("Enter a number: "))
    print(n[m])
except ValueError:
    print("ValueError")
except IndexError:
    print("IndexError")
#4
try:
    file = open("myresult.txt", "r")
except FileNotFoundError:
    print("File not found")
#5
#???
#6
try:
    a = int(input("Enter first number "))
    b = int(input("Enter second number "))
    c = int(input("Enter third number "))
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Invalid input")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid input")
    average = (a + b + c) / 3
    print("The average is", average)
except ValueError as z:
    print(z)
except Exception:
    print("Something went wrong")