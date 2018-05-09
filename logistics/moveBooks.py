import os as os
from shutil import copyfile
import sys

def recurseP(path,pd):
    ogs = os.listdir(path)
    for x in ogs:
        if(x[-3:] == "zip"):
            copyfile(path+x,pd+x)
        else:
            recurseP(path+x+"/")
            
print (os.getcwd())
pathtoBook1 = sys.argv[1]
pathtoDest = sys.argv[2]

recurseP(pathtoBook1,pathtoDest)

'''
ogs = (os.listdir(pathtoBook))
testing = (os.listdir("/home/avanroi1/projGutenburg/books.NOBACKUP/aleph.gutenberg.org/1/0/0/0/10001/"))
'''


            
