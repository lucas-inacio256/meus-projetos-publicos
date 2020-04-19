###############################################################################

## author: Lucas santos
## version: 1.1
## Python 3.6.5 | UTF-8

## Required Modules:
##   google-api-python-client
##   google-auth-httplib2
##   google-auth-oauthlib

print('='*50)
print('Importing modules.')
from backup import get_datetime
from backup import zipFolder
from backup import authBuild
from backup import uploadFile
from backup import remove
print('Completed!\n')

###############################################################################

def main():
    date = get_datetime()
    print('Backup day: {}\n'.format(date))

    folder_path = 'C:/?' # Paste the folder path here
    zip_file_name = 'Backup({}).zip'.format(date)
    mime = 'application/zip'

    print('Zipping Folder: {}'.format(folder_path))
    zipped = zipFolder(folder_path, zip_file_name)
    if zipped:
        print('Completed!\n')

        print('Authenticating upload.')
        scopes = ['https://www.googleapis.com/auth/drive.file']
        auth_path = 'auth/'
        service = authBuild(scopes, auth_path)
        print('Completed!\n')

        print('Uploading.')
        file_id = uploadFile(service, zip_file_name, zip_file_name, mime)
        print('Completed!')
        print('File ID: {}\n'.format(file_id))

        print('Removing zip file: {}\n'.format(zip_file_name))
        remove(zip_file_name)
        print('Completed!\n')

        print('Backup completed!\n')

main()
input('Press any key to exit>>')
