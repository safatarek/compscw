from csEncryption import XOR, IP, FP, permute, fFunction, BitsToText

def DecryptedBlock(block64b, roundkeys):
    ipresult=permute(block64b, IP)
    L=ipresult[:32]
    R=ipresult[32:]
    for i in range(15, -1, -1):
        NewL=R
        fFoutput=fFunction(R, roundkeys[i])
        NewR=XOR(L, fFoutput)
        L=NewL
        R=NewR
    swap=R+L
    Plain64b=permute(swap, FP)
    return Plain64b

from csEncryption import XOR, IP, FP, permute, fFunction, BitsToText

def DecryptedBlock(block64b, roundkeys):
    ipresult=permute(block64b, IP)
    L=ipresult[:32]
    R=ipresult[32:]
    for i in range(15, -1, -1):
        NewL=R
        fFoutput=fFunction(R, roundkeys[i])
        NewR=XOR(L, fFoutput)
        L=NewL
        R=NewR
    swap=R+L
    Plain64b=permute(swap, FP)
    return Plain64b

def DecryptedMessage(CipherBits, roundkeys):
    PlainText=''
    for i in range(0, len(CipherBits), 64):
        BlockBits=CipherBits[i:i+64]
        PlainBlockBits=DecryptedBlock(BlockBits, roundkeys)
        BlockText=BitsToText(PlainBlockBits)
        PlainText+=BlockText
    PlainText=PlainText.rstrip('\x00')
    return PlainText
