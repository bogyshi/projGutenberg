import os as os
import zipfile as zpf
import sys

pathtoBooks = sys.argv[1]

for x in os.listdir(pathtoBooks):
    if(not(x[-6:]=="-8.zip") and not (x == "ASCII")):
        zipr = zpf.ZipFile(pathtoBooks+x,'r')
        zipr.extractall(pathtoBooks+"ASCII/")
        zipr.close()
