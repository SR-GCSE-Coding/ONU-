def signUp():
    #account = input("Do you have an account? ")

    #if account == ('no'):
    #    signup = input('Do you want to create an account? ')

    #    if signup == ('no'):
    #       print('You can\'t play')


    #    else:
        print('Please enter your details')

        username = input('Enter your username \n> ')
        password = input('Enter your password \n> ')

        with open ('logIn.txt', 'a') as filehandle:
            filehandle.write('%s\n%s\n' %(username, password))

def logIn():
    print('Enter your login details')

    user = input('>')
    password = input('>')

    if user !=

    

def accountCheck():
    account1 = input('Does player one have an account? ')

    if account 1 == ('no'):
        signUp()

    if account1 == ('yes'):
        logIn()


    account2 = input('Does player two have an account? ')

    if account2 == ('no'):
        signUp()

    if account2 == ('yes'):
        logIn()
        
    
