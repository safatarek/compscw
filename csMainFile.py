from cskeys import genkey, gen16keys
from csEncryption import EncryptedMessage
from csDecryption import DecryptedMessage

def Main():
    key64=genkey()
    print('Random 64-bit key:')
    print(key64)

    roundkeys=gen16keys(key64)

    PlainText=input('Please enter your message to get encrypted:')

    CipherBits=EncryptedMessage(PlainText, roundkeys)
    print('Ciphertext Bits:')
    print (CipherBits)

    DecryptedText=DecryptedMessage(CipherBits, roundkeys)
    print('Decrypted Text:')
    print(DecryptedText)

if __name__ == "__main__":
    Main()