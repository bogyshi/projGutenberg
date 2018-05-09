import datetime

class Book:
    def __init__(self):
        self.length=0
        self.title=""
        self.bid = 0 
        self.language=""
        self.hasCharacters=False
        self.rawBook=None
        self.releaseDate=None
        self.chars=None
        self.newLineRatio=0.0
        self.singQuotChar=0
        self.doubQuotChar=0

    def createBook(self,l,lang,hc,txt,rd,titl,bd,nlr,sqc,dqc):
        self.length=l
        self.title=titl
        self.bid = bd
        self.language=lang
        self.hasCharacters=hc
        self.rawBook=txt
        self.releaseDate=rd
        self.chars=None
        self.newLineRatio=nlr
        self.singQuotChar=sqc
        self.doubQuotChar=dqc

    def toString(self):
        part1 = "Title: " + self.title + "\n"
        part2 = "Gutenberg ID: " + str(self.bid)+"\n"
        part3 = "Language: " + self.language+"\n"
        part4 = "Length (in characters): " + str(self.length)+"\n"
        if(self.releaseDate is not None):
            part5 = "Gutenberg Release Date: " + str(self.releaseDate.timetuple()[0]) + " " + str(self.releaseDate.timetuple()[1]) + " " + str(self.releaseDate.timetuple()[2])
        else:
            part5 = "Gutenberg Release Date: N/A"
        part6=""
        if(self.hasCharacters):
            #for x in self.chars:
            #    part6+=x+"\n"
            pass
        else:
            part6 = ""
        return part1+part2+part3+part4+part5+part6
    
    def getCharacters(self):
        self.chars=[]
