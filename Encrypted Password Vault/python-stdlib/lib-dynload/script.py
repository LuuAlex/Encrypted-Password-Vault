import os
import base64
import csv

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def initialize(path):
    path = path + "/EncryptedPasswordVault_UserData"
    return path + "/passwordData.csv", path + "/salt.txt"

# Password Tool - convertPassword to key
def convertPassword(password, salt):
    password = password.encode()
    if not isinstance(salt, bytes):
        salt = str(salt).encode()
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt= salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

# Password Tool - create Fernet
def getFernet(path, password):
    passwordDataPath, saltPath = initialize(path)

    with open(saltPath, 'rb') as enc_file:
        salt = enc_file.read()
        enc_file.close()
    key = convertPassword(password, salt)
    return Fernet(key), salt



def create_csv(path, password):
    passwordDataPath, saltPath = initialize(path)

    # Create the Key
    salt = os.urandom(16)
    key = convertPassword(password, salt)
    saltKey = open(saltPath, 'wb')
    saltKey.write(salt)
    saltKey.close()
    f = Fernet(key)

    # Create the File
    fileX = open(passwordDataPath, 'wb')
    fileX.write("".encode()) # delete previous data
    fileX.close()
    file = open(passwordDataPath, 'rb')

    # Encrypt and Rewrite the File
    encrypt(path, password, file.read().decode())
    file.close()

def changePassword(path, password, newPassword):
    passwordDataPath, saltPath = initialize(path)
    decrypted = decrypt(path, password)

    # Create the Key
    salt = os.urandom(16)
    saltKey = open(saltPath, 'wb')
    saltKey.write(salt)
    saltKey.close()

    # Encrypt and Rewrite the File
    encrypt(path, newPassword, decrypted)
    
def decrypt(path, password):
    # Get Key and Paths
    passwordDataPath, saltPath = initialize(path)
    f, salt = getFernet(path, password)
        
    # Decrypt File
    enc_file = open(passwordDataPath, 'rb')
    encrypted = enc_file.read()
    enc_file.close()
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Failed to decrypt")
        return None
    return decrypted.decode().replace("\r\n", "\\r\\n")

def encrypt(path, password, dataString):
    # Get Key and Paths
    passwordDataPath, saltPath = initialize(path)
    f, salt = getFernet(path, password)

    # Encrypt File
    encrypted = f.encrypt(dataString.encode())
    encrypted_file = open(passwordDataPath, 'wb')
    encrypted_file.write(encrypted)
    encrypted_file.close()



def read(path, password):
    return decrypt(path, password)

# write new password entry; newDataEntry = [KEY, USER, PASS]
def write(path, password, newDataEntry):
    # Decrypt File
    writer = decrypt(path, password)

    # Add New Entry
    writer = writer + "\r\n"
    for x in newDataEntry:
        writer = writer + str(x) + ","
    writer = writer[0:len(writer) - 1]
    
    # Encrypt and Rewrite the File
    encrypt(path, password, writer)

# deletes entry with "key", so cannot have duplicate keys
def delete(path, password, key):
    # Decrypt File
    writer = decrypt(path, password)

    # Delete Entry
    pos1 = writer.find("\r\n" + key + ",")
    pos2 = writer.find("\r\n", pos1 + 2)
    if pos2 == -1:
        pos2 = len(writer)
    if pos1 == -1:
        return
    writer = writer[0:pos1] + writer[pos2:]
    
    # Encrypt and Rewrite the File
    encrypt(path, password, writer)

    
