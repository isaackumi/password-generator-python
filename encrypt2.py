import string


def encryptMessage():
    line = '====='*10
    print(line)
    
    print()
    print('This program contains an encryption algorithm')
    print('that can encrypt and decrypt any message you type.')
    print()
    print(line)
    print()
    print('Press 1 to encrypt and 2 to decrypt')
    print()
    choice = input('Do you want to Encrypt or Decrypt: ')
    encrypt=''
    alphabet = string.ascii_lowercase
    key = 5
    if choice == '1':
          
        message = input('Enter a message to encrypt :  ')
        print()
        
        for char in message:
            position =  alphabet.find(char)
            newposition = (position+key)%26
            
            encrypt+=alphabet[newposition]
        return print(f'Your encrypted message is : {encrypt}')
       

    
    elif choice == '2':
            
        decrypt=''
        message = input('Enter a message to decrypt :  ')
        print()
        

        for char in message:
            pos =  alphabet.find(char)
            newpos = (pos-key)%26
            decrypt+=alphabet[newpos]
        print(f'Your decrypted message is : {decrypt}')
    
    else:
        print('Number out of range')
        print('Please press 1 to encrypt and 2 to decrypt')
        print('Program exiting .....')
encryptMessage()      





