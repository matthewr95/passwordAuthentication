from cryptography.fernet import Fernet

def generateKey():
  key = Fernet.generate_key()
  print(key)

def encryptPassword(key):
  cipherKey = key
  cipherSuite = Fernet(cipherKey)
  cipheredText = cipherSuite.encrypt(b"")    #required to be bytes
  print(cipheredText)
