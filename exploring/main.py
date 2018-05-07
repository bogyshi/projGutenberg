from reading import allFiles
import os as os
import calendar
import sys
import re

patternTR = " truth (\w*\W*)* truth"
months = dict((v,k) for k,v in enumerate(calendar.month_name))

def parseReleaseDate(book):
    '''
    grabs the release date of the book from the entire string
    '''
    patternRD = "Release Date: (\w*) (\d|\d\d), (\d\d\d\d)"
    patternRD2 = "Release Date:"
    prog=re.compile(patternRD)
    pos = re.search(prog,book)
    #use months to map neames, case sensitivity may be a thing
    month = (pos.group(1))
    day = pos.group(2)
    year = pos.group(3)
path = sys.argv[1]
x = allFiles(path)
everything  = open(x[1], 'r').read()
parseReleaseDate(everything)
'''
for fbook in x:
    everything  = open(fbook, 'r').read()
    parseReleaseDate(everything)
    '''

#source 1: https://stackoverflow.com/questions/3418050/month-name-to-month-number-and-vice-versa-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    
