###############################################################################

## author: Lucas santos
## version: 1.0
## Python 3.6.5 | UTF-8

## Modules required:
##   google-api-python-client
##   google-auth-httplib2
##   google-auth-oauthlib

print('='*50)
print('Importing modules.')
from backup import *
print('Completed!\n')

###############################################################################

def main():
    date = get_datetime()
    print('Backup day: {}\n'.format(date))

    folder_path = 'C:/?' # Paste the folder path here
    zip_file_name = 'Backup({}).zip'.format(date)
    mime = 'application/zip'

    print('Zipping Folder: {}'.format(folder_path))
    zipFolder(folder_path, zip_file_name)
    print('Completed!\n')

    print('Authenticating upload.')
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    AUTH_PATH = 'auth/'
    service = authBuild(SCOPES, AUTH_PATH)
    print('Completed!\n')

    print('Uploading.')
    file_id = uploadFolder(service, zip_file_name, zip_file_name, mime)
    print('Completed!')
    print('Folder ID: {}\n'.format(file_id))

    print('Removing zip file: {}\n'.format(zip_file_name))
    remove(zip_file_name)
    print('Completed!\n')

    print('Backup completed!\n')

main()
input('Press any key to exit>>')
