import os as os
import zipfile as zpf

pathtoBooks = "/import/linux/home1/avanroi1/projGutenburg/books.NOBACKUP/allBooks/"

for x in os.listdir(pathtoBooks):
    if(not(x[-6:]=="-8.zip") and not (x == "ASCII")):
        zipr = zpf.ZipFile(pathtoBooks+x,'r')
        zipr.extractall(pathtoBooks+"ASCII/")
        zipr.close()
