import os
import base64
import csv

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


# Password Tool - convertPassword to key
def convertPassword(password, salt):
    password = bytes(password, "utf-8")
    if not isinstance(salt, bytes):
        salt = bytes(str(salt), "utf-8")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt= salt,
        iterations=480000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password))

def getFernet(password):
    with open('passwordData.csv', 'rb') as enc_file:
        salt = enc_file.readline()[-1]
    key = convertPassword(password, salt)
    return Fernet(key), salt



def create_csv(password):
    # Create the Key
    salt = os.urandom(16)
    key = convertPassword(password, salt)
    f = Fernet(key)

    # Create the File
    file = open('passwordData.csv', 'w+', newline='')

    # Encrypt and Rewrite the File
    encrypted = f.encrypt(bytes(file.read(), "utf-8"))
    with open('passwordData.csv', 'w+', newline='') as encrypted_file:
        encrypted_file.write(str(encrypted))
        encrypted_file.writelines(str(salt)) # add salt
    
    
def read(password):
    # Get Key
    f, salt = getFernet(password)
        
    # Decrypt File
    with open('passwordData.csv', 'rb') as enc_file:
        encrypted = enc_file.read()
    try:
        decrypted = f.decrypt(encrypted)
    except:
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

    
    


