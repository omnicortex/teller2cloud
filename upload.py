from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()

# Create GoogleDrive instance with authenticated GoogleAuth instance.
drive = GoogleDrive(gauth)

file2 = drive.CreateFile()
file2.SetContentFile('tokens.csv')
file2.Upload()
print('Created file %s with mimeType %s' % (file2['title'],
file2['mimeType']))
