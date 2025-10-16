from cryptography.fernet import Fernet

def generateKey():
  key = Fernet.generate_key()
  print(key)

def encryptPassword(key):
  cipherKey = key
  cipherSuite = Fernet(cipherKey)
  cipheredText = cipherSuite.encrypt(b"")    #required to be bytes
  print(cipheredText)

def savePassword(cipheredText, binFile):
  with open(binFile, 'wb') as file_object:
    file_object.write(cipheredText)

def getPasswod(key, binFile):
  with open(binFile, 'rb') as file:
    for line in file:
      encryptedPassword = line
      
  cipherSuite = Fernet(key)
  uncipherText = (cipherSuite.decrypt(encryptedPassword))
  plainTextPassword = bytes(uncipherText).decode("utf-8")
  # print(plainTextPassword)
  return plainTextPassword


generateKey()

key = ""
encryptPassword(key)

cipheredText = ""
binFile = ".bin"
savePassword(cipheredText, binFile)

getPassword(key, binFile)
