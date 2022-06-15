# RansomWhale
Utilizing Docker and Python to look at the fundamentals of how an attacker may Encrypt and Decrypt files on a system.

## Installation
`git clone https://github.com/imtaylorgriffin/RansomWhale.git`  
To a directory of your choice.

## Usage
Move to the directory you cloned to, then:
`cd RansomWhale`  
At the moment we can use:   
`docker build -t ransom .`  
`docker run -i -t ransom /bin/sh`   
Once we're inside, we start at the /app directory. From there, you can `cd ~` to explore your home folder files.
In the home folder, you can `cat` a few of the files to see their orignal text.

After you finish exploring, you can `cd /app/` to get back to our Python scripts.   
**EncRansomWhale.py** will encrypt all files on the user's home folder  
**DecRansomWhale.py** will decrypt all of the encrypted files in the home folder.   

Use `python EncRansomWhale.py` to start the Ransomware.  
After it finishes you can `cd ~` to go back to your home directory.   
The first thing you may notice is that the Extensions have changed, which is a good sign for us (bad sign for the victim) that the files have been altered. If you `cat` a file of you choice, you will see that we are now given a line of text that does not make any sense, success!  

If you `cd /app/` again you may notice that there is a secret.key file that was created from EncRansomWhale, **DecRansomWhale.py** makes use of this file to decrypt our victim's files.   
Next, use `python DecRansomWhale.py` to decrypt the files. After you can `cd ~` back to you home directory and `cat` a file, if everything was succesful, you should get the original output!

## Python Scripts   
Both of the scripts make use of Cryptography, specifically Fernet, which can be found here: https://cryptography.io/en/latest/fernet/   
They both contain comments throughout the code but I will explain a few of the key parts in greater detail.
### EncRansomWhale.py 
#### Generating the Key
<p>
    <img src="/githubStuff/enc keygen.png"  />
</p>
This is the unique key that we will utilize to Encrypt and Decrypt our victim's files. It uses Fernet's generate_key() method which can be found <a href="https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L46-L48">Here</a> which we will then save as secret.key   

#### Encrypting the files
<p>
    <img src="/githubStuff/enc.png"  />
</p>    
Now for the fun part, for encrypting we give it all of the files in our list, read their bytes, and pass them to Fernet's encrypt method found <a href="https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L50-L51">Here</a>      

I wanted to make this a little more fun, so I added my own file extension '.RansomWhale.mp4' to support this, I grabbed the filename and extension, removed the old file after reading and saving it's bytes to f_bytes_encrypted, and then wrote it's bytes to our new file encFile, which is the filename + custom extension.

### DecRansomWhale.py
#### Opening the key
<p>
    <img src="/githubStuff/dec key.png"  />
</p>
Here is where we open the victim's key, read it in, and pass it to Fernet.

#### Decrypting the files
<p>
    <img src="/githubStuff/dec.png"  />
</p>
For decrypting the files we read in the bytes of all the encrypted files in our list, pass them to Fernet's decrypt method which can be found <a href="https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py#L82-L90">Here</a> then we'll replace the file's '.RansomWhale.mp4' extension with it's original extension, write the decrypted bytes to our file with the original extension, and delete our old encrypted file.
