def key(KEY):
    for i in range(len(plain)):
        if plain[i] == ' ' or plain[i] == '!' or plain[i] == ':' or plain[i] == '_':
            KEY+='0'
        else:
            KEY+='8'
    return KEY

def encrypt(plain,KEY):
    encrypt = ''
    for i in range(len(plain)):
        encrypt+=chr((ord(plain[i]))-int(KEY[i]))
    return encrypt
    
plain = "See you in the next InCTF! All the very best for all the challenges! And your flag: leet_1337_leet"
ENCRYPT,KEY = '',''
KEY = key(KEY)
ENCRYPT = encrypt(plain,KEY)
print KEY
print ENCRYPT
