def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division (x,y):
    return x/y

print("Select Operation:" )
print("1.Addition") 
print("2.Subtraction")
print("3.Multiplication") 
print("4.Division")

option=int(input("Select Operation (1-4): "))

x=int(input("Enter first number: "))
y=int(input("Enter second number: "))


if option ==1:
    print(x,'+',y,'=',addition(x,y))
elif option==2:
    print(x,'-',y,'=',subtraction(x,y))
elif option==3:
    print(x,'*',y,'=',multiplication(x,y))
elif option==4:
    print(x,'/',y,'=',division(x,y))
    