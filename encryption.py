from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Based On: NeuralNine's Password Manager in Python
# TODO: Convert to class

# Variables
salt : bytes = b'D\xe8\x81\xc1|;#2\x87\xadj\xbc\x1c,\xef\xa6\x11\x10}c\x1e\xfa\r\x06\xbem\x15\xe5^\xb7\xfc*'
defaultKey : bytes = b'W\xdf\x11\xac]\x16\\\x92\xd3>\xc2\x03\xc7\x88\xc54\xd5\x17B\xc3mq\xbc\x03\x96E\x16\x11\x02\x84\xef\x17'
key : bytes

# Functions
def getKey(password, salt=salt):
    key = PBKDF2(password, salt, dkLen=32)
    return key

def generateSalt():
    # salt = generate_random_bytes(32)
    return

def encrypt(key, mode, filePath, message):
    if (mode == False):
        key = defaultKey

    message = bytes(message, 'utf-8')
    cipher = AES.new(key, AES.MODE_CBC)
    encryptData = cipher.encrypt(pad(message, AES.block_size))

    with open(filePath, 'wb') as file:
        file.write(cipher.iv)
        file.write(encryptData)

def decrypt(key, mode, filePath):
    if (mode == False):
        key = defaultKey

    with open(filePath, 'rb') as file:
        iv = file.read(16)
        decryptData = file.read()
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    original = unpad(cipher.decrypt(decryptData), AES.block_size)
    original = str(original, 'UTF-8')
    return original