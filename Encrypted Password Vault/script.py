import os
import base64
import csv

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


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

def getFernet(password):
    with open('salt.txt', 'rb') as enc_file:
        salt = enc_file.read()
        enc_file.close()
    key = convertPassword(password, salt)
    return Fernet(key), salt



def create_csv(password):
    # Create the Key
    salt = os.urandom(16)
    key = convertPassword(password, salt)
    saltKey = open('salt.txt', 'wb')
    saltKey.write(salt)
    saltKey.close()
    f = Fernet(key)

    # Create the File
    file = open('passwordData.csv', 'rb')

    # Encrypt and Rewrite the File
    encrypted = f.encrypt(file.read())
    encrypted_file = open('passwordData.csv', 'wb')
    encrypted_file.write(encrypted)

    file.close()
    encrypted_file.close()
    
    
def read(password):
    # Get Key
    f, salt = getFernet(password)
        
    # Decrypt File
    enc_file = open('passwordData.csv', 'rb')
    encrypted = enc_file.read()
    enc_file.close()
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Failed to decrypt")
        return None

    return decrypted.decode()


# write new password entry; newDataEntry = [KEY, USER, PASS]
def write(password, newDataEntry):
    # Get Key
    f, salt = getFernet(password)

    # Decrypt File
    enc_file = open('passwordData.csv', 'rb')
    encrypted = enc_file.read()
    enc_file.close()
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Failed to decrypt")
        return None

    # Add New Entry
    writer = decrypted.decode()
    for x in newDataEntry:
        writer = writer + str(x) + ","
    writer = writer[0:len(writer) - 1]
    writer = writer + "\r\n"
    endoded = writer.encode()
    
    # Encrypt and Rewrite the File
    encrypted = f.encrypt(endoded)
    encrypted_file = open('passwordData.csv', 'wb')
    encrypted_file.write(encrypted)
    encrypted_file.close()

def delete(password, key):
    # Get Key
    f, salt = getFernet(password)

    # Decrypt File
    enc_file = open('passwordData.csv', 'rb')
    encrypted = enc_file.read()
    enc_file.close()
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Failed to decrypt")
        return None

    # Delete Entry
    writer = decrypted.decode()
    pos1 = writer.find("\r\n" + key + ",") + 2
    if pos1 == -1:
        pos1 = writer.find(key + ",")
    print(pos1)
    pos2 = writer.find("\r\n", pos1) + 2
    print(pos2)
    writer = writer[0:pos1] + writer[pos2:]
    endoded = writer.encode()
    
    # Encrypt and Rewrite the File
    encrypted = f.encrypt(endoded)
    encrypted_file = open('passwordData.csv', 'wb')
    encrypted_file.write(encrypted)
    encrypted_file.close()

    
    


