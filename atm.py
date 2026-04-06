balance = 1000
Button = 0
while Button != 4:
    print ('1. check balance',
            '2. Deposit',
            '3. Withdraw',
            '4. Exit')
    print ('please enter ur choice')
    Button = input()
    if int(Button) == 1:
       print('Your Balance is', balance)
    elif int(Button) ==2:
        print ('please enter the money u want to depsoit')
        money =input()
        balance = balance + int(money)
    elif int(Button) == 3:
        print ('enter the amount u want to withdraw')
        money = input()
        balance = balance- int(money)
        if balance < 0:
            print ('Dame Desu')
            balance = balance + int(money)
    elif int(Button) == 4:
        break
    else:
        print('wrong choice')
        continue
        
print('thank u for using our atm')