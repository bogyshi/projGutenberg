import os as os

def allFiles(path):
    alf = os.listdir(path)
    newls = []
    for x in alf:
        if(x[-3:]=="txt"):
            newls.append(path+x)
    return newls
