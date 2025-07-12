a = int(input("enter the number "))
b = int(input("Enter the number "))
try:
    c = a/b
except ZeroDivisionError as e:
    print("error occured cannot divide the number by zero")
    c= None
except ValueError as e:
    print("wrong value type")
    c = None
except Exception as e:
    print("something invaid occured")
    c=None
print("the result is ",c)
    