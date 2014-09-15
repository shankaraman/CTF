import os,sys,zipfile

original_file = "73168.zip"

while True:
try:
    original_file = zipfile.ZipFile(original_file)

for contents in original_file.namelist():
    password = contents[0:contents.find('.')]

original_file.setpassword(password)
original_file.extractall()

original_file = password+'.zip'

except:
   break
