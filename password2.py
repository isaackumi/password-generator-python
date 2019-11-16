import random



def passwordGenerator():
  
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"$%^&*()'
    numbers = '0123456789'

    #print(letters)
    lenght = int(input('Enter the lenght of your password: '))
    numberOfletters = int(input('Enter number of letters : '))
    numberOfNumbers =int( input('Enter number of numbers:  '))
    
    let = ''
    num = ''



    if lenght > 5 and lenght <= 25:

        for _ in range(numberOfNumbers):
            num+= random.choice(numbers)
            

        for  _ in range(numberOfletters):
            let+=random.choice(letters)

    print(let+num)
passwordGenerator()
