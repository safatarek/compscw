PC1= [
    57,49,41,33,25,17,9,
     1,58,50,42,34,26,18,
    10, 2,59,51,43,35,27,
    19,11, 3,60,52,44,36,
    63,55,47,39,31,23,15,
     7,62,54,46,38,30,22,
    14, 6,61,53,45,37,29,
    21,13, 5,28,20,12, 4
] #permutation tables

PC2= [
     14,17,11,24, 1, 5,
     3,28,15, 6,21,10,
    23,19,12, 4,26, 8,
    16, 7,27,20,13, 2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]
shiftby=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1] #shift schedule

import random #so it wont be one set key

def genkey(): #key generation
    key= ''
    for k in range(64):
        key+=str (random.randint(0,1))
    return key

def permute(bits, table): #to order the bits
    result=''
    for index in table:
        result+=bits [index - 1]
    return result

def leftshiftbt28(bt28, p):
    return bt28[p:]+bt28[:p]

def gen16keys(keybits):
    key56=permute(keybits, PC1) #to remove parity bits =56 bits
    C=key56[:28] #splits them to 2 parts
    D=key56[28:]

    keys16=[] #to generate 16 iterations

    for shiftn in shiftby:
        C=leftshiftbt28(C,shiftn)
        D=leftshiftbt28(D,shiftn)

        CD= C+D
        Key=permute(CD, PC2) #into 48 bits
        keys16.append(Key)
    return keys16
