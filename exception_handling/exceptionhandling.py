# some exceptions
#1/0 (this will be not possible)
#'abc'+2 (same as this as this will also be not possible)
x = input("enter the number")
y = input("enter the number")
try:
    z= x / int(y)
except ZeroDivisionError as e:
    print("exception occured",e)
    z= None
except TypeError as e:
    print("exception type",type(e).__name__)#type(e)give the type of exception and .__name__ would provide us the name of the exception
    z=None
    
print("division is ",z)