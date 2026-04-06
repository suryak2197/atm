def number1():
    n1 = int(input("enter the 1st number"))
    return n1
def number2():
    n2 = int (input("enter the 2nd number"))
    return n2
    
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul (n1,n2):
    return n1*n2
def div (n1,n2):
    if n2== 0:
        return None
    else:
        return n1/n2
print('1. Add')
print('2. Sub')
print('3. Multiplication')
print('4. Divison')
print('5.Exit')

operation = 0
while operation != 5:
    try:
        operation = int(input('What do u want to do'))
    except:
        print('error')
    if operation == 1:
        a = number1()
        b = number2()
        result= add(a,b)
        print (result)
    elif operation ==2:
        a = number1()
        b = number2()
        result= sub(a,b)
        print(result)
    elif operation ==3:
        a = number1()
        b = number2()
        result= mul(a,b)
        print(result)
    elif operation ==4:
        a = number1()
        b = number2()
        if b == 0:
            print('Error, cant divide with 0')
        else:
            result= div(a,b)
            print(result)
    elif operation ==5:
        print('thank u for using the calculator')
        break

    
    else:
        print('Error, try again')
        continue
    
