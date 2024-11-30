import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)

for file in os.listdir('export'):
    filename = os.fsdecode(file)
    file = drive.CreateFile()
    file.SetContentFile(filename)
    file.Upload()
    print('Created file %s with mimeType %s' % (file['title'], file['mimeType']))
