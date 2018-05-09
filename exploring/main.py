from reading import allFiles
import book as bk
import os as os
import calendar
import sys
import re
import datetime
import time


#NOTE FATSA language fiels are large and take much longer to process
'''
old getLen function, did not work for older / different formats of the start book lines
)
'''
months = dict((v,k) for k,v in enumerate(calendar.month_name))

def blnToAcRatio(document):
    '''
    Computes the ratio of empty new lines to total lines
    '''
    btwnLines = "\n\n"
    allLines = "\n"
    tp = re.compile(r'\r\n\r\n')
    dn = re.compile(r'\r\n')
    tottop = float(len(re.findall(tp,document))) 
    totbot = float(len(re.findall(dn,document)))
    
    return tottop/totbot

def getBookText(book,fid):
    '''
    constructs book objects
    '''
    spot = fid.rfind("/")
    bid = fid[spot+1:-4]
    temp = bk.Book()
    patternStrt = "\\*\\*\\* START OF THIS PROJECT GUTENBERG EBOOK ((.*)*) \\*\\*\\*"
    patternStrt2 = "\\*\\*\\*START OF THE PROJECT GUTENBERG EBOOK ((.*)*)\\*\\*\\*"
    
    patternEnd = "\\*\\*\\* END OF THIS PROJECT GUTENBERG EBOOK ((.*)*) \\*\\*\\*"
    patternEnd2 = "\\*\\*\\*END OF THE PROJECT GUTENBERG EBOOK ((.*)*)\\*\\*\\*"

    titlere = "Title: (.*)"
    prog = re.compile(r'Title: (.*)')
    post = re.search(prog,book)
    title = post.group(1) # doesnt handle multiline titles
    stopPoint = 0
    x = book.find("*** START OF THIS PROJECT GUTENBERG EBOOK")
    if(x == -1):
        x = book.find("***START OF THE PROJECT GUTENBERG EBOOK")
    y = book.rfind("*** END OF THIS PROJECT GUTENBERG EBOOK")
    if(y == -1):
        y = book.rfind("***END OF THE PROJECT GUTENBERG EBOOK")
    prog = re.compile(patternStrt)
    post = re.search(prog,book)
    bookbeg = 0
    bookend = 0
    booklen = 0
    rawBook = None
    bookbeg = x+len(title)
    bookend = y
    rawBook = book[bookbeg:bookend] #not quite right due to deprecated titles and such
    booklen = bookend-bookbeg
    lang = parseLanguage(book)
    hasChars = CorA(rawBook)
    rd = parseReleaseDate("whocares",book)
    nlr = blnToAcRatio(rawBook)
    dqc = convoLen(rawBook)
    sqc = convoLen2(rawBook)
    temp.createBook(booklen,lang,hasChars,rawBook,rd,title,bid,nlr,dqc,sqc)
    return temp

def getTitle(book,gbid):
    '''
    UNUSED: old getTitle method, no longer used
    '''
    patternStrt = "\\*\\*\\* START OF THIS PROJECT GUTENBERG EBOOK ((.*)*) \\*\\*\\*"
    prog = re.compile(patternStrt)
    title = re.search(prog,book).group(1)
    startpos = book.find("*** START OF THIS PROJECT GUTENBERG EBOOK " + title + " ***")
    endpos = book.rfind("*** END OF THIS PROJECT GUTENBERG EBOOK " + title + " ***")
                    
                    
def CorA(book):
    '''
    USELESS: was supposed to determine if the book contains characters or actors, but really jsut sees if the word actor appears
    '''
    prog = re.compile(r'\bcharacter\b')
    res = re.search(prog,book)
    if(res is None):
        return None
    else:
        return res


def convoLen(book):
    '''
    Determines amount of dialogue by summing space between double quotes
    '''
    lenConvo = 0
    curPos=0
    while(curPos > -1):
        startpos=book.find("\"",curPos)
        if(startpos == -1):
            return lenConvo
        endpos = book.find("\"",startpos)+1
        if(endpos==-1):
            print("ERROR in book " + book[:700])
        lenConvo += endpos-startpos
        curPos = endpos+1
    return lenConvo

def convoLen2(book):
    '''
    Determines amount of dialogue by summing space between single quotes
    '''
    lenConvo = 0
    curPos=0
    while(curPos > -1):
        startpos=book.find("\'",curPos)
        if(startpos == -1):
            return lenConvo
        endpos = book.find("\'",startpos)+1
        if(endpos==-1):
            print("ERROR in book " + book[:700])
        lenConvo += endpos-startpos
        curPos = endpos+1
    return lenConvo


def getLen(book):
    '''
    Gets length of book, 
    NOTE: we can determine which book is largest relatively easy by just 
    grabbing the text file that has the largest file size.
    '''
    startpos = book.find("*** START OF THIS PROJECT GUTENBERG EBOOK")
    endpos = book.rfind("*** END OF THIS PROJECT GUTENBERG EBOOK")
    if(startpos == -1):
        startpos = book.find("***START OF THE PROJECT GUTENBERG EBOOK")
        endpos=book.rfind("***END OF THE PROJECT GUTENBERG EBOOK")
    if(startpos==-1 or endpos == -1):
        print("ERROR on book: " + book[:500])
    return (endpos - startpos)

def parseLanguage(book):
    '''
    grabs the language of the book
    '''
    patternLN = "Language: ((.*)*)"
    prog=re.compile(patternLN)
    pos = re.search(prog,book)
    #use months to map neames, case sensitivity may be a thing
    if(pos is None):
        return None
    else:
        return pos.group(1)

def isTT(book):
    '''
    searches for three instances of the word 'truth', if so returns true
    05/07/18 VERY SLOW (also wasnt correct)
    05/08/18 much faster
    '''
    prog= re.compile(r'\btruth\b',re.IGNORECASE)
    count=0
    tpos=0
    while(True):
        if(count == 3):
            return True
        pos = re.search(prog,book[tpos:])
        if pos is None:
            return False
        else:
            tpos = tpos + pos.start()+len("truth")+1
            count+=1
        


def parseReleaseDate(name, book):
    '''
    grabs the release date of the book
    '''
    patternRD = "Release Date: (\w*) (\d|\d\d), (\d\d\d\d)"
    prog=re.compile(patternRD)
    pos = re.search(prog,book)
    #use months to map neames, case sensitivity may be a thing
    try:
        month = months[(pos.group(1))]
        day = int(pos.group(2))
        year = int(pos.group(3))
    except:
        return None
    return datetime.datetime(year,month,day)

path = sys.argv[1]
x = allFiles(path)
allDatetimes=dict() #IMPROVEMENT: Create tree structure to travers and store resutls of datetimes faster
#variables for determining average releaste date
avgRD = 0.0
mostCommonRD = None
#variables for determining most common Release Date
rdc = 0
nEnglish = 0.0
#list for all books holding truth twice
bookwtt=[]
#handles longest book location
longestBook = None
lbc = 0
#handles convo length
lConvoB = None
lconvo = 0
#list of books that have characters
bookwa=[]
#bookWithGreatestRatio
bookmnlr =None
mnlr = 0.0
#bookWithMaxSingleQuoteChars
bookmsqc =None
msqc = 0.0
#bookWithMaxDoubleQuoteChars
bookmdqc =None
mdqc = 0.0
#entire list of books
allBooks=[]
counter = 0
'''
attempt to label / find files with a character or role list

test = "\bPERSONS REPRESENTED\b"
plz = re.compile(test)
for fbook in x:
    everything  = open(fbook, 'r').read()
  
    idk = re.search(plz,everything)
    if(idk is not None):
        print(idk.group(0))
'''
for fbook in x:
    everything  = open(fbook, 'r').read()
    allBooks.append(getBookText(everything,fbook))
    ld = convoLen(everything)
    if(allBooks[counter].newLineRatio > mnlr):
        mnlr = allBooks[counter].newLineRatio
        bookmnlr = allBooks[counter]
    if(allBooks[counter].singQuotChar > msqc):
        msqc = allBooks[counter].newLineRatio
        bookmsqc = allBooks[counter]
    if(allBooks[counter].doubQuotChar > mdqc):
        mdqc = allBooks[counter].newLineRatio
        bookmdqc = allBooks[counter]
    if(allBooks[counter].length>lbc):
        longestBook = allBooks[counter]
        lbc = longestBook.length
    if(isTT(everything)):
        bookwtt.append(fbook)
    if(allBooks[counter].language.strip() == "English"):
        nEnglish+=1
    temp = allBooks[counter].releaseDate
    if(temp is not None):
        avgRD+=time.mktime(temp.timetuple())
        if(temp in allDatetimes):
            allDatetimes[temp]+=1
            if(allDatetimes[temp]>rdc):
                mostCommonRD = temp
                rdc = allDatetimes[temp]
        else:
            allDatetimes[temp]=1
    if(allBooks[counter].hasCharacters is not None):
        bookwa.append(allBooks[counter])
    counter+=1


avgRD = (time.gmtime(int(avgRD/len(allBooks))))

print("The average release date is: " + str(avgRD.tm_year))
print("The most common release date is: " + str(mostCommonRD.timetuple()[0]) + " " + str(mostCommonRD.timetuple()[1]) + " " + str(mostCommonRD.timetuple()[2]))
print("The number of books with the word truth in it at least 3 times: " + str(len(bookwtt)))
print("Ratio of english to non english books is: " + str(nEnglish/len(allBooks)))
print("Total number of books checked books checked:" + str(len(allBooks))+"\n")
print("Longest book: " + longestBook.toString()+"\n")
print("Book with the highest NLR is:\n" + bookmnlr.toString()+"\n")
print("Book with the highest character count w/ single quotes is:\n" + bookmsqc.toString()+"\n")
print("Book with the highest character count w/ double quotes is:\n" + bookmdqc.toString()+"\n")
#print("books with characters: ")
#print(len(bookwa))
#print(bookwa[10].title)
#print(len(allBooks))
#print(allBooks[1].toString)
#these two values make a lot of sense, nice!
#There are some books with no text in them, ex file 11755, its a musical score but nothing printed.

