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
### EncRansomWhale  

### DecRansomWhale

