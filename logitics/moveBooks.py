import os as os
from shutil import copyfile

def recurseP(path):
    ogs = os.listdir(path)
    for x in ogs:
        if(x[-3:] == "zip"):
            copyfile(path+x,"/import/linux/home1/avanroi1/projGutenburg/books.NOBACKUP/allBooks/"+x)
        else:
            recurseP(path+x+"/")
            
print (os.getcwd())
pathtoBook1 = "/import/linux/home1/avanroi1/projGutenburg/books.NOBACKUP/aleph.gutenberg.org/1/1/"
pathtoBook2 = "/import/linux/home1/avanroi1/projGutenburg/books.NOBACKUP/aleph.gutenberg.org/1/2/"

recurseP(pathtoBook1)
recurseP(pathtoBook2)

'''
ogs = (os.listdir(pathtoBook))
testing = (os.listdir("/home/avanroi1/projGutenburg/books.NOBACKUP/aleph.gutenberg.org/1/0/0/0/10001/"))
'''


            
