from cryptography.fernet import Fernet

def generateKey():
  key = Fernet.generate_key()
  print(key)
