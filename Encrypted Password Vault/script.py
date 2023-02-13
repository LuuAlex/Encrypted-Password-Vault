import os
import base64
import csv

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def initialize(pDP, sP):
    return pDP + "/passwordData.csv", sP + "/salt.txt"

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
def getFernet(pDP, sP, password):
    passwordDataPath, saltPath = initialize(pDP, sP)

    with open(saltPath, 'rb') as enc_file:
        salt = enc_file.read()
        enc_file.close()
    key = convertPassword(password, salt)
    return Fernet(key), salt



def create_csv(pDP, sP, password):
    passwordDataPath, saltPath = initialize(pDP, sP)

    # Create the Key
    salt = os.urandom(16)
    key = convertPassword(password, salt)
    saltKey = open(saltPath, 'wb')
    saltKey.write(salt)
    saltKey.close()
    f = Fernet(key)

    # Create the File
    file = open(passwordDataPath, 'rb')

    # Encrypt and Rewrite the File
    encrypted = f.encrypt(file.read())
    encrypted_file = open(passwordDataPath, 'wb')
    encrypted_file.write(encrypted)

    file.close()
    encrypted_file.close()

def changePassword(pDP, sP, password, newPassword):
    passwordDataPath, saltPath = initialize(pDP, sP)
    decrypted = decrypt(pDP, sP, password)

    # Create the Key
    salt = os.urandom(16)
    key = convertPassword(newPassword, salt)
    saltKey = open(saltPath, 'wb')
    saltKey.write(salt)
    saltKey.close()
    f = Fernet(key)

    # Encrypt and Rewrite the File
    encrypted = f.encrypt(decrypted.encode())
    encrypted_file = open(passwordDataPath, 'wb')
    encrypted_file.write(encrypted)

    encrypted_file.close()
    
def decrypt(pDP, sP, password):
    # Get Key and Paths
    passwordDataPath, saltPath = initialize(pDP, sP)
    f, salt = getFernet(password)
        
    # Decrypt File
    enc_file = open(passwordDataPath, 'rb')
    encrypted = enc_file.read()
    enc_file.close()
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Failed to decrypt")
        return None

    return decrypted.decode()

def encrypt(pDP, sP, password, dataString):
    # Get Key and Paths
    passwordDataPath, saltPath = initialize(pDP, sP)
    f, salt = getFernet(password)

    # Encrypt File
    encrypted = f.encrypt(dataString.encode())
    encrypted_file = open(passwordDataPath, 'wb')
    encrypted_file.write(encrypted)
    encrypted_file.close()



def read(pDP, sP, password):
    # Get Key and Paths
    passwordDataPath, saltPath = initialize(pDP, sP)
    f, salt = getFernet(password)
        
    # Decrypt File
    enc_file = open(passwordDataPath, 'rb')
    encrypted = enc_file.read()
    enc_file.close()
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Failed to decrypt")
        return None

    return decrypted.decode()

# write new password entry; newDataEntry = [KEY, USER, PASS]
def write(pDP, sP, password, newDataEntry):
    # Decrypt File
    writer = decrypt(pDP, sP, password)

    # Add New Entry
    for x in newDataEntry:
        writer = writer + str(x) + ","
    writer = writer[0:len(writer) - 1]
    writer = writer + "\r\n"
    
    # Encrypt and Rewrite the File
    encrypt(pDP, sP, password, writer)

# deletes entry with "key", so cannot have duplicate keys
def delete(pDP, sP, password, key):
    # Decrypt File
    writer = decrypt(pDP, sP, password)

    # Delete Entry
    pos1 = writer.find("\r\n" + key + ",") + 2
    if pos1 == -1:
        pos1 = writer.find(key + ",")
    pos2 = writer.find("\r\n", pos1) + 2
    writer = writer[0:pos1] + writer[pos2:]
    
    # Encrypt and Rewrite the File
    encrypt(pDP, sP, password, writer)

    