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
    try:
        decrypted = f.decrypt(encrypted)
    except:
        print("Failed to decrypt")
        return

    return decrypted


# write new password entry; newDataEntry = [KEY, USER, PASS]
def write(password, newDataEntry):
    decrypted = read(password)
    if (not decrypted):
        return
    writer = decrypted
    writer.writerows(newDataEntry)

    f, salt = getFernet(password)
    
    # Encrypt and Rewrite the File
    encrypted = f.encrypt(writer)
    with open('passwordData.csv', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
        csv.writer(encrypted_file).writerows(["SALT", salt]) # add salt

    
    


