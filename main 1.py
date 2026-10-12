# Program For A Mini Calculator

print("\n\t\t\t\t\tWelcome To Our Calculator !")

#Choose The Operation You want to Perform

print("\t\t\t\t\tChoose The Operation ~")

print("\n\t\t\t\t\t1. Addition")
print("\t\t\t\t\t2. Subtraction")
print("\t\t\t\t\t3. Multiplication")
print("\t\t\t\t\t4. Division")

choice = int(input("Enter Your Choice :  "))


if choice==1:
    print("\t\t\t\t\tADDITION (+)")
    num1 = int(input("Enter 1st Number :  "))
    num2 = int(input("Enter 2nd Number :  "))
    print("\t\t\t\t\tThe Sum of both the numbers is",num1+num2)

elif choice ==2:
    print("\t\t\t\t\tSUBTRACTION (-)")
    int1 = int(input("Enter 1st Number :  "))
    int2 = int(input("Enter 2nd Number :  "))
    print("\t\t\t\t\tThe Difference of both the number is",int1-int2)

elif choice ==3:
    print("\t\t\t\t\tMultiplication (*)")
    mul1 = int(input("Enter 1st Number :  "))
    mul2 = int(input("Enter 2nd Number :  "))
    print("\t\t\t\t\tThe Product of both the numbers is",mul1*mul2)

elif choice ==4:
    print("\t\t\t\t\tDivision")
    div1 = int(input("Enter 1st Number :  "))
    div2 = int(input("Enter 2nd Number :  "))
    print("\t\t\t\t\tThe Quotient of both the Number is",div1/div2)

else:
    print("\t\t\t\t\tInvalid Choice !")
    print("\t\t\t\t\tTry Typing - 1 , 2 , 3 , 4")