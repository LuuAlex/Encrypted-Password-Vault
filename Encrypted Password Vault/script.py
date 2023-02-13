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

# Password Tool - create Fernet
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

def changePassword(password, newPassword):
    decrypted = decrypt(password)

    # Create the Key
    salt = os.urandom(16)
    key = convertPassword(newPassword, salt)
    saltKey = open('salt.txt', 'wb')
    saltKey.write(salt)
    saltKey.close()
    f = Fernet(key)

    # Encrypt and Rewrite the File
    encrypted = f.encrypt(decrypted.encode())
    encrypted_file = open('passwordData.csv', 'wb')
    encrypted_file.write(encrypted)

    encrypted_file.close()
    
def decrypt(password):
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
    writer = decrypt(password)

    # Add New Entry
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

# deletes entry with "key", so cannot have duplicate keys
def delete(password, key):
    # Get Key
    f, salt = getFernet(password)

    # Decrypt File
    writer = decrypt(password)

    # Delete Entry
    pos1 = writer.find("\r\n" + key + ",") + 2
    if pos1 == -1:
        pos1 = writer.find(key + ",")
    pos2 = writer.find("\r\n", pos1) + 2
    writer = writer[0:pos1] + writer[pos2:]
    endoded = writer.encode()
    
    # Encrypt and Rewrite the File
    encrypted = f.encrypt(endoded)
    encrypted_file = open('passwordData.csv', 'wb')
    encrypted_file.write(encrypted)
    encrypted_file.close()

    
    


