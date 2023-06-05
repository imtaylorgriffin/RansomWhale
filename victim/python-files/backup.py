import os
import shutil #archive files


    
# grab the home directory
home_dir = os.path.expanduser("~")
print(home_dir)

# simulate backing up to an external drive
backup_dir = os.path.abspath("/mnt/myBackupDrive")


# if the backup directory doesn't exist, make the directory
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print("Creating backup directory")

for root, dirs, files in os.walk(home_dir):
    # Skip subdirs, just want to show the idea
    if root != home_dir:
        continue
    
    
    for file in files:
        
        file_path = os.path.join(root, file)
        
        relative_path = os.path.relpath(file_path,home_dir)
        
        bak_file_path = os.path.join(backup_dir,file)#relative_path)
        bak_directory = os.path.dirname(bak_file_path)
        
        if not os.path.exists(bak_directory):
            os.makedirs(bak_directory)
        
        
        # shutil.copy2 copies the file and its contents but also tries to preserve the timestamps, file permissions, 
        # and other file attributes as much as possible. Good for creating an exact copy of the file, including its metadata.
        shutil.copy2(file_path,bak_file_path) 
        ##
        
        
        print(f"{file_path} backed up to {bak_file_path}")
            
            