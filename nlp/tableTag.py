from nltk.stem import Porter
import cPickle

stemmer = Porter()

words = ["happy","quiet","calm","clear","false"]

VOWELS = ["a","e","i","o","u"]

FILENAME = "ling120.tex"

BEGIN_DOC = r'''
\documentclass{article}
\usepackage[english]{babel}
\begin{document}
\begin{center}
\begin{tabular}{'''

SEP = " & "
PREFIX = 0
SUFFIX = 1

BACK = 'b'
QUIT = 'q'
EDIT = 'e'
PRINT_ROW = 'pr'
PRINT_ALL = 'pa'
CONTROL_TAGS =[BACK,QUIT,EDIT,PRINT_ROW,PRINT_ALL]
TAGS = ["?","*",'']

ALIGNL = " | l"
ALIGN = ALIGNL

END_TABLE_ROW = r" \\ \hline" +"\n"

END_DOC = r'''
    \hline
    \end{tabular}
\end{center}
\end{document}"
'''

def addPrefix(prefix,w):
    return prefix + w

def addSuffix(suffix,w):
    #so we get falseness instead of falsness
    if w[-1] not in VOWELS:
        w = stemmer.stem(w)

        #remove doubled letters
        #so happiify won't happen
        if w[-1] == suffix[0]:
            w = w[:-1]

    return w + suffix

transforms = [
            (0,"un"),
            (1,"ness"),
            (1,"ify"),
            (0,"to "),
            (1,"ly")
             ]

def makeRow(w,transforms):
    res = []
    for (funct,morph) in transforms:
        if funct == PREFIX:
            res.append( addPrefix(morph,w) )
        else:
            res.append( addSuffix(morph,w) )

    return res

def toTopRowForm( (funct,morph) ):
   if funct == PREFIX:
       return (morph + "++" )
   elif funct == SUFFIX:
       return ( "++" + morph )

def makeTopRow(transforms,hw):
    return SEP.join(  map(toTopRowForm, transforms) )

def makeTable(data,hw):
    hw.write( BEGIN_DOC )
    hw.write(ALIGN * len(words) + "|}\n" + END_TABLE_ROW)

    hw.write( makeTopRow(transforms,hw) + END_TABLE_ROW  )

    for row in data:
       hw.write( SEP.join( row ) + r" \\ \hline" + "\n")

    hw.write( END_DOC )

def makeData(words,transforms):
    mat = []
    for w in words:
       mat.append( makeRow(w,transforms) )

    return mat

def moveBack(row,col):
   col -= 1
   if col < 0:
       col += 1
       row -= 1
       if row < 0:
           print "can't go back more (at start)"
           return (0,0)

   return row,col

def tagUsage():
   print '''please type
'*' for not ok
'?' for questionable
<enter> for OK,
'b' for back one,
'q' for quit,
'e' to replace word(edit)
'pr' to print current row
'pa' to print all \n'''

def tagData(data):
    nRows = len(data)
    nCols = len( data[0] )
    #for row in xrange(nRows):
        #for col in xrange(nCols):
    process = True

    row = 0
    col = 0
    while process:

        print data[row][col]
        s = raw_input()

        while s not in TAGS and s not in CONTROL_TAGS:
            tagUsage()
            s = raw_input()

        if s in CONTROL_TAGS:
            if s == BACK:
                row,col = moveBack(row,col)
                continue
            elif s == QUIT:
                print "quiting editing"
                return data
            elif s == EDIT:
                print "input string to replace " + data[row][col]
                data[row][col] = raw_input()
                s = ''
            elif s == PRINT_ROW:
                print "\n"
                print data[row]
                print "\n"
                continue
            elif s == PRINT_ALL:
                print "\n"
                for stuff in data: #for row, but didn't want name clash
                    print stuff
                print "\n"
                continue

        data[row][col] = addPrefix(s,data[row][col])

#goto next and do bounds test
        col += 1
        if col >= nCols:
            row += 1
            col = 0
            if row >= nRows:
                print "you've tagged all the words, quiting now"
                process = False

    return data

def saveData(mat):
    s = ''
    while s not in ["y","n"]:
        s = raw_input("would you like to save the data in a file?y/n\n")

    if s == "y":
        filename = validateFilename(".p")
        cPickle.dump(mat,open(filename,'wb'))

def validateFilename(suffix):
    s = ''
    while s != 'y':
        filename = raw_input("What is the filename?\n")
        filename += suffix
        s = raw_input("\nthe file will be '" + filename + "' is that ok y/n?\n")
        if s == "y":
            return filename

def loadPickle():
    print "the data must be a .p pickle file"
    print "this program saves the data as these filetypes"
    filename = validateFilename(".p")
    return cPickle.load( open(filename,"rb"))

def main():
    words = ["happy","quiet","calm","clear","false"]

    print "We are going to write a latex file."
    filename = validateFilename(".tex")
    hw = open(filename,'w')


    print "we must get words and define transformations! \n"
    print "these are the default words:"
    print str(words) + "\n"
    s = raw_input("would you like to use the defaults(y) or use other words?(n) y/n\n")
    while s not in ["y","n"]:
        s = raw_input("would you like to use the defaults(y) or use other words?(n) y/n")

    if s == "n":
        while s not in ["l","i","d","f"]:
            s = raw_input("\nDo you want to load data (l),interactively add words(i),load a cvs file?(f),or use default(d)\n")
            if s == "l":
                data = loadPickle()
    else:
        data = makeData(words,transforms)

    saveData(data) #ask if want to save untransformed data

    s = ''
    while s != "y" and s != "n":
        s = raw_input("\nWould you like to tag the data? y/n\n")
        if s == "y":
            tagUsage()
            tagData(data)


    saveData(data) #ask if want to save transformed data

    print "writing latex file!"
    makeTable(data,hw)

    hw.close()


