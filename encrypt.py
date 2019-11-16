import random, math, string


def encryptMessage():
    message = input('Enter a message:  ')
    key = 5
    encrypt=''
    alphabet = string.ascii_lowercase
    #alphabet = '5d5f\c0\8\/ab|$cdef/@ghijk&*lmn$o&pq\/rst0uvw^xyz\xcb\xc4x9d2$a7'

    for char in message:
        position = alphabet.find(char)
        newposition = (position+key)%26
        encrypt+=alphabet[newposition]
    print('Your encrypted message is :',encrypt)
    return encrypt
        




def decryptMessage():
    encrypt=encryptMessage()
    #message = input('Enter a message to decrypt:  ')
    key = 5
    decrypt=''
    alphabet = string.ascii_lowercase
    #alphabet = '5d5f\c0\8\/ab|$cdef/@ghijk&*lmn$o&pq\/rst0uvw^xyz\xcb\xc4x9d2$a7'

    for char in encrypt:
        position = alphabet.find(char)
        newposition = (position-key)%26
        decrypt+=alphabet[newposition]
    print('Your decrypted message is : ',decrypt)
    return decrypt
    
        


decryptMessage()


