""" 
        
        Looks like something missing here!

"""

def decrypt(key,cipher):
	decipher = ''
	for i in range(len(cipher)):
		decipher+=chr(ord(cipher[i])+int(key[i]))
	return decipher


key = '88808880880888088880888880088808880888808888088808880888088888888880088808888088880088880888808888'
cipher = 'K]] qgm af l`] f]pl Af;L>! 9dd l`] n]jq Z]kl ^gj Ydd l`] [`Ydd]f_]k! 9f\ qgmj ^dY_: d]]l_)++/_d]]l'
flag = decrypt(key,cipher)
print flag
