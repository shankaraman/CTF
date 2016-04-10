fd = open("config.enc","r")
fd_data = fd.read()
hex_data = ''
for i in fd_data:
#    print hex(ord(i)),'\t',ord(i),'\t',i,'\t', bin(ord(i))
    hex_data += str(hex(ord(i))).replace("0x","")
print hex_data

import binascii
y = binascii.unhexlify(hex_data)
print(''.join([chr(ord(a)^0xff) for a in y]))
