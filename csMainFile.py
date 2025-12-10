from cskeys import genkey, gen16keys #to avoid rewriting the functions
from csEncryption import EncryptedMessage
from csDecryption import DecryptedMessage

def Main():
    key64=genkey() #generates keys
    print('Random 64-bit key:')
    print(key64)

    roundkeys=gen16keys(key64)

    PlainText=input('Please enter your message to get encrypted:') #gets the main text from the user

    CipherBits=EncryptedMessage(PlainText, roundkeys) #encrypts the text
    print('Ciphertext Bits:')
    print (CipherBits)

    DecryptedText=DecryptedMessage(CipherBits, roundkeys) #decrypts it back into original
    print('Decrypted Text:')
    print(DecryptedText)

if __name__ == "__main__":
    Main()
