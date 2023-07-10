from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Based On: NeuralNine's Password Manager in Python
# TODO: Convert to class

# Variables
salt : str  # -> generate_random_bytes(32)
key : bytes # -> PBKDF2(password, salt, dkLen=32)
message : bytes # -> b""

# Functions
def generateKey(salt, password):
    # key = PBKDF2(password, salt, dkLen=32)
    pass

def generateSalt():
    # salt = generate_random_bytes(32)
    pass

def loadKey(password):
    pass

def encrypt(message, key):
    # wb
    # cipher = AES.new(key, AES.MODE_CBC)
    # ciphered_data = cipher.encrypt(pad(message, AES.block_size))
    # f.write(cipher.iv)
    # f.write(ciphered_data)
    pass

def decrypt(message, key):
    # rb
    # iv = f.read(16)
    # decrypt_data = f.read() 
    # cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    # original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
    pass