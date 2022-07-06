# <img src="/githubStuff/rw.png"  />
Utilizing Docker and Python to look at the fundamentals of how an attacker may Encrypt and Decrypt files on a system.

## Installation
`git clone https://github.com/imtaylorgriffin/RansomWhale.git`  
To a directory of your choice.

## Updates
See debug/changelog.txt for things being added.   
See commands_resources.txt to see different commands and additional info.

## Usage
Move to the directory you cloned to, then:
`cd RansomWhale`  
We can use: `docker-compose up -d`  

### 1. Encryption
#### Attacker Terminal:   
It is important to go into the Attacker terminal first using:
`docker container exec -it attacker /bin/sh`   
The Attacker has a python script that will listen on port 5001 for incoming key information and write the file as `private_key.pem`. 
You can start this script by using `python listener.py`
#### Victim Terminal: 
`docker container exec -it victim /bin/sh`    
The Victim has the ransomware, which will encrypt all files in their home directory with RSA, and secretly send the private key over to the Attacker.   
Once we're inside the Victim terminal, we start at the ~/app directory. From there, you can `cd ~` to explore your home folder files.
In the home folder, you can `cat` a few of the files to see their orignal text.
I reccomend opening up the two terminals side by side. 

After you finish exploring, you can `cd ~/app/` to get back to the Ransomware.   
Use `python v2ransomPackage.py` to start the Ransomware. It shows the files being encrypted and also a ransom note! 
On the Attacker terminal, you'll notice that we obtained our private_key! It's saved in the attacker home folder as `private_key.pem`

On the Victim terminal, After it finishes you can `ls` there is now a public_key.pem file that was created from our Ransomware, this was created from the private key to encrypt all of our files. `cd ~` to go back to the home directory.   
The first thing you may notice is that the Extensions have changed, which is a good sign for us (bad sign for the victim) that the files have been altered. If you `cat` a file of you choice, you will see that we are now given a line of text that does not make any sense, success!  

### 2. Email Simulation (work in progress)
To simulate the paying and recieving part I have created a basic email simulation. You can `cd ~/email` on both the Attacker and Victim.
On the Victim side: To make an email `vi email_i-paid-ransom` after you type it you can save it and do `sh send.sh` which will "send" it over to our Attacker's inbox
On the Attacker side: The victim's email is in the inbox, to send the key, you can `mv ~/private_key.pem .` then `vi email_here-is-the-key` after typing the email_ file, you can send using sh send.sh  The key is in Victim's inbox/attachments.  

### 3. Decryption
To Decrypt, `mv email/inbox/attachments/private_key.pem app/.` and then `python v2ransomPackage.py` If successful, you should see Successfully Decrypted messages.



## RansomWhale Info   
The python script make use of Cryptography, specifically RSA, which can be found here: https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/#   
They both contain comments throughout the code, I will explain a few of the key parts in greater detail. 
#### File Targeting
<p>
    <img src="/githubStuff/target.png"  />
</p>
If RansomWhale sees a private_key, it will enter decryption mode where it will try to use the key to decrypt the data.
If a private_key is not found, it will continue to encrypt the files.

#### Generating the Attacker's Key
<p>
    <img src="/githubStuff/enc keygen.png"  />
</p>
We have to first start with generating the private key since the Cryptography module needs it to make the public key. A few options here stand out, like public_exponent and key_size, those are the reccommended default values for the private key because they "will help defend against weaknesses discovered in the future."  

#### Sending the Attacker's Key
<p>
    <img src="/githubStuff/key-transfer.png"  />
</p>
Here is where we'll secretly send the attacker the private key needed to decrypt the files. This will read all of the bytes in the key file and send them over, after it is done, the Ransomware will delete the key so the victim can't use it.

#### Encrypting the files
<p>
    <img src="/githubStuff/enc.png"  />
</p>    
Now for the fun part, for encrypting we give it each of the files in our list, read their bytes, and pass them to Public Key's encrypt method using the reccommended defalut values.      

I wanted to make this a little more fun, so I added my own file extension '.RansomWhale.mp4' to support this, I grabbed the filename and extension, removed the old file after reading and saving it's bytes to f_bytes_encrypted, and then wrote it's bytes to our new file encFile, which is the filename + custom extension.

#### Decrypting the files
<p>
    <img src="/githubStuff/dec.png"  />
</p>
For decrypting the files, if we found a private_key, we read in the bytes of all the encrypted files in our list, pass them to the Private Key's decrypt method, then we'll replace the file's '.RansomWhale.mp4' extension with it's original extension, write the decrypted bytes to our file with the original extension, and delete our old encrypted file.
