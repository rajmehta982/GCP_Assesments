
from google.cloud import storage
import os


storage_client = storage.Client()
bucket = storage_client.get_bucket('raj-mehta--bucket')

DESTINATION_FOLDER = ''
DOWNLOAD_FOLDER = 'folder1'


blobs = bucket.list_blobs()


for b in blobs:
        
    fold = DESTINATION_FOLDER + ''
        
    if b.name.startswith(DOWNLOAD_FOLDER) and b.name[-1] != '/':
            
        folder_struct = b.name.split('/')
            
        for folder in folder_struct[:-1]:
            fold += folder + '/'
            try:
                os.mkdir(fold)
            except Exception as e:
                pass
            
        b.download_to_filename(fold + folder_struct[-1])

print('Bucket "folder1" has been replicated!')