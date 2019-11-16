import random



def passwordGenerator():
    #letters = string.ascii_letters
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!"$%^&*()'
    #print(letters)
    lenght = int(input('Enter the lenght of your password: '))
    numberOfletters = int(input('Enter number of letters : '))
    numberOfSymbols =int( input('Enter number of symbols:  '))
    
    let = ''
    sym = ''
    num = ''



    if lenght > 5 and lenght <= 25:
        
        for _ in range(lenght):
            let += random.choice(letters)
            sym += random.choice(symbols)
            num += random.choice(numbers)

        print(let+sym+num)

    else:
        print('Password lenght should be between 6 and 25')



passwordGenerator()
