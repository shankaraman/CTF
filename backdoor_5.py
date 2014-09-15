import pickle

class Clue(object):

    def __init__(self, name, killer):
        self.name = name
        self.killer = killer

    def getKiller(self):
        print decode(self.killer)

    def encode(s):
        a = []
        b = []
        for i in range(len(s)):
            t = ord(s[i])
            x1, x2 = divide(t)
            a.append(x1)
            b.append(x2)
        return (a, b)

    def decode(s):
        a, b = s
        final = []
        for i in range(len(a)):
            t1 = a[i]
            t2 = b[i]
            p = combine(t1, t2)
            x = chr(p)
            final.append(x)
        print final
        return ''.join(final)

     def divide(t):
        t = str(t)
        return (''.join([ t[x] for x in range(0, len(t), 2) ]), ''.join([ t[x] for x in range(1, len(t), 2) ]))

    def combine(t1, t2):
        p = []
        for i in t1:
            p += [i]

        for i in range(len(t2)):
            p.insert(2 * i + 1, t2[i])

        return int(''.join(p))

secret = (['9', '9', '11', '12', '11', '9', '14', '11', '13', '1', '9', '14', '11', '9', '11', '10', '15', '16', '14', '17', '9', '16', '11', '14', '1', '12', '4', '1', '4', '9', '9', '9', '19', '9', '15', '10', '9', '9', '1', '6', '18', '17', '11', '1', '12', '4', '1', '9', '9', '9', '9', '17', '15', '18', '16', '15', '10', '9', '9', '1', '11', '9', '16', '11', '9', '16', '1', '12', '5', '1', '7', '16', '12', '5', '1', '8', '12', '5', '1', '4', '10', '12', '5', '1', '8', '3', '17', '15', '18', '18', '11', '14', '3', '1', '12', '5', '1', '4', '4', '18', '12', '5', '1', '8', '3', '5', '3', '1', '12', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '4', '4', '1', '9', '8', '3', '5', '3', '1', '12', '4', '4', '1', '9', '8', '3', '5', '3', '1', '12', '4', '5', '1', '9', '8', '3', '5', '3', '1', '12', '4', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '4', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '4', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '4', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '4', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '4', '5', '1', '9', '13', '4', '4', '1', '9', '13', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '4', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '4', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '4', '1', '9', '8', '3', '4', '5', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '5', '1', '9', '4', '18', '12', '5', '5', '1', '8', '3', '5', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '3', '1', '12', '5', '5', '1', '9', '8', '3', '5', '3', '1', '12', '5', '5', '1', '9', '13', '4', '5', '1', '9', '13', '4', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '16', '12', '5', '5', '1', '15', '8', '3', '10', '9', '19', '11', '3', '1', '12', '5', '4', '1', '4', '4', '18', '12', '5', '4', '1', '13', '4', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '5', '1', '9', '13', '4', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '5', '5', '1', '9', '13', '4', '4', '1', '9', '13', '4', '5', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '5', '5', '1', '9', '8', '3', '4', '5', '3', '1', '12', '5', '4', '1', '9', '8', '3', '4', '4', '3', '1', '12', '5', '4', '1', '9', '4', '18', '12', '5', '5', '1', '13', '4', '5', '1', '9', '13', '5', '5', '1', '9', '13', '4', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '4', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '13', '5', '5', '1', '9', '16', '12', '5', '5', '1', '15', '9', '4'],['9', '9', '1', '1', '2', '5', '1', '0', '0', '0', '5', '1', '0', '9', '1', '1', '1', '1', '1', '1', '9', '1', '1', '1', '0', '1', '8', '0', '0', '9', '5', '5', '0', '7', '0', '1', '5', '5', '0', '7', '0', '1', '0', '0', '1', '9', '0', '9', '5', '5', '8', '1', '0', '0', '1', '0', '1', '5', '5', '0', '1', '8', '0', '0', '9', '1', '0', '1', '0', '0', '8', '1', '1', '1', '0', '2', '1', '2', '0', '0', '0', '1', '3', '0', '3', '9', '0', '0', '0', '0', '0', '1', '9', '0', '1', '4', '0', '0', '0', '0', '1', '5', '0', '3', '9', '6', '9', '0', '1', '6', '0', '7', '3', '9', '9', '9', '9', '0', '1', '7', '0', '7', '3', '9', '9', '7', '9', '0', '1', '9', '8', '0', '7', '3', '9', '1', '9', '0', '1', '9', '9', '0', '7', '3', '9', '5', '9', '0', '1', '9', '0', '0', '7', '3', '9', '7', '9', '0', '1', '9', '1', '0', '7', '3', '9', '9', '2', '9', '0', '1', '9', '2', '0', '7', '3', '9', '9', '6', '9', '0', '1', '9', '3', '0', '7', '3', '9', '9', '9', '9', '0', '1', '9', '4', '0', '7', '3', '9', '9', '6', '9', '0', '1', '9', '5', '0', '7', '3', '9', '9', '9', '9', '0', '1', '9', '6', '0', '7', '0', '9', '9', '0', '7', '0', '6', '0', '7', '3', '9', '9', '3', '9', '0', '1', '9', '7', '0', '7', '3', '9', '9', '8', '9', '0', '1', '0', '8', '0', '7', '3', '9', '9', '8', '9', '0', '1', '0', '9', '0', '7', '3', '9', '9', '6', '9', '0', '1', '0', '0', '0', '7', '3', '9', '9', '9', '9', '0', '1', '0', '1', '0', '7', '0', '0', '1', '0', '2', '0', '3', '9', '2', '9', '0', '1', '0', '3', '0', '7', '3', '9', '9', '9', '0', '1', '0', '4', '0', '7', '3', '9', '8', '9', '0', '1', '0', '5', '0', '7', '3', '9', '0', '9', '0', '1', '0', '6', '0', '7', '0', '9', '0', '0', '7', '0', '9', '0', '0', '7', '0', '0', '4', '0', '7', '0', '0', '4', '0', '7', '0', '0', '4', '0', '7', '0', '0', '5', '0', '7', '0', '0', '4', '0', '7', '0', '0', '6', '0', '7', '0', '0', '6', '0', '7', '0', '0', '5', '0', '7', '0', '0', '5', '0', '7', '0', '0', '5', '0', '7', '0', '0', '5', '0', '7', '0', '0', '5', '0', '7', '1', '1', '0', '7', '0', '1', '3', '9', '1', '7', '0', '0', '9', '0', '1', '1', '8', '0', '0', '0', '0', '1', '1', '9', '0', '0', '9', '0', '0', '7', '3', '9', '9', '9', '9', '0', '1', '1', '0', '0', '7', '0', '9', '1', '0', '7', '3', '9', '9', '8', '9', '0', '1', '1', '1', '0', '7', '3', '9', '9', '3', '9', '0', '1', '1', '2', '0', '7', '3', '9', '9', '8', '9', '0', '1', '1', '3', '0', '7', '3', '9', '9', '1', '9', '0', '1', '1', '4', '0', '7', '0', '9', '9', '0', '7', '0', '9', '0', '0', '7', '3', '9', '9', '9', '9', '0', '1', '1', '5', '0', '7', '3', '9', '9', '2', '9', '0', '1', '1', '6', '0', '7', '3', '9', '9', '4', '9', '0', '1', '1', '7', '0', '7', '3', '9', '9', '6', '9', '0', '1', '2', '8', '0', '7', '3', '9', '9', '9', '9', '0', '1', '2', '9', '0', '7', '0', '0', '1', '2', '0', '0', '0', '9', '0', '0', '7', '0', '0', '4', '0', '7', '0', '9', '0', '0', '7', '0', '0', '4', '0', '7', '0', '0', '5', '0', '7', '0', '0', '4', '0', '7', '0', '0', '5', '0', '7', '0', '0', '6', '0', '7', '0', '9', '0', '0', '7', '0', '0', '6', '0', '7', '0', '0', '4', '0', '7', '0', '0', '4', '0', '7', '0', '0', '5', '0', '7', '0', '0', '5', '0', '7', '1', '1', '2', '1', '0', '1', '8', '6'])

    def touchFile():
        with open('.clue', 'w') as f:
            f.write(decode(secret))


f = open('clue','r').read()
flag = pickle.loads(f)
print flag.getKiller()
