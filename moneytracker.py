#comment time to increase the size of this god damn file cs discod think its empty
def exp():
    expense = []
    spent = input("please enter thing u spent money on")
    while True:
        try:
            money = int(input("please enter money spent"))
            break
        except:
            print("Error u cant enter alphabet")
    expense.append(spent)
    expense.append(money)
    return expense


log= []
i = 0
while True:
    print("1. Add Expenses \n 2.Show Expenses \n 3. Show Total Spent \n 4. Exit")
    while True:
        try:
            n = int(input("What Would u Like to do:"))
            break
        except:
            print ('error, please enter a number')
            
    if n == 1: 
        log.append(exp())
    elif n == 2:
        print(log)
    elif n == 3:
        spent = 0
        for i in range(len(log)):
            spent += int(log[i][1])
        print(spent)
    elif n == 4:
        break
    else:
        print ('please enter a number between 1-4')
        continue
    
            
#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum                 

    
