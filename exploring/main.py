from reading import allFiles
import os as os
import sys
import re

patternTR = " truth (\w*\W*)* truth"

def parseReleaseDate(book):
    '''
    grabs the release date of the book from the entire string
    '''
    patternRD = "Release Date: \w* (\d|\d\d), \d\d\d\d"
    patternRD2 = "Release Date:"
    prog=re.compile(patternRD)
    pos = re.search(prog,book)
    print(pos.group(0))
path = sys.argv[1]
x = allFiles(path)
everything  = open(x[1], 'r').read()
parseReleaseDate(everything)
'''
for fbook in x:
    everything  = open(fbook, 'r').read()
    parseReleaseDate(everything)
    '''
    
    
