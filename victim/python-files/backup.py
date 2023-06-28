import os
import shutil #archive files
import argparse #add -r to "restore" files



# command line args
parser = argparse.ArgumentParser(description='Backup and restore app')
parser.add_argument('-r', '--restore', action='store_true', help='Restore files')
args = parser.parse_args()
    
# grab the home directory
home_dir = os.path.expanduser("~")

# simulate backing up to an external drive
backup_dir = os.path.abspath("/mnt/myBackupDrive")


# get command line args
if args.restore:
    home_dir, backup_dir = backup_dir, home_dir
    print('Restoring files from backup')
else:
    print(f'backing up files')
    
    
# if the backup directory doesn't exist, make the directory
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)
    print("Mounting to backup drive")
    
for file in os.listdir(home_dir):
    file_path=os.path.join(home_dir, file)
    if os.path.isfile(file_path):
        shutil.copy2(file_path,backup_dir)
        print(f'{file_path} {"restored" if args.restore else "backed up to"} {backup_dir}')   
    
        