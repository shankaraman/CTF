import os,sys
while True:
    os.system('bzip2 -d pack.tar.bz2')
    os.system('tar -xvf pack.tar')
    os.system('rm pack.tar')

