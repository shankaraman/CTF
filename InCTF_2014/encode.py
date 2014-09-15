# Challenge Name dump.exe
def encode(b):
    # Encode Mapping : f -> a | 3 -> 1 
    for i in range(len(b)):
        if b[i] == 'f':
            b[i] = 'a'
        elif b[i] == '3':
            b[i] = '1'
    return b

def decode(c):
    # Decode Mapping : a -> f | 1 -> 3 
    for i in range(len(c)):
        if c[i] == 'a':
            c[i] = 'f'
        elif c[i] == '1':
            c[i] = '3'
    return c

def list2string(lst):
    string=''
    for i in range(len(lst)):
        string+=lst[i]
    return string

flag = "3768335f626930735f70343535773072645f69735f48545450343034"
encoded_flag = ''
flag_list,encoded_return,decoded_return = [],[],[]
for i in range(len(flag)):
    flag_list.append(flag[i])
encoded_return = encode(flag_list)
print "Encoded String:"+list2string(encoded_return)+"\t"+"Decodes:"+list2string(encoded_return).decode("hex")
decoded_return = decode(encoded_return)
print "Decoded String:"+list2string(decoded_return)+"\t"+"Decodes:"+list2string(encoded_return).decode("hex")
