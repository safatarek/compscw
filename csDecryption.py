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
