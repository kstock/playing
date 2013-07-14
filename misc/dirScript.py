import os,sys,pickle
FILEPATH = "/home/kstock/Music/"

macpath = 'macMusic.p'
savepath = 'asusMusic.p'
testpath = 'asusMusicPRIME.p'
testpath2 = 'asusMusicPRIME2.p'

#FILEPATH = "."

def makeData(filename,filepath=FILEPATH ):

    a = {os.path.basename(root):files for root,dirs,files in os.walk(filepath) }
    pickle.dump(a, open(filename, 'wb'))

def fixData(filename):
    data = pickle.load(open(filename, 'rb'))
    data = {os.path.basename(path):songs for (path,songs)
                                        in data.iteritems()}

    pickle.dump(data, open(filename, 'wb'))

def songDiff(left,right):
    leftUniq = []
    #rightUniq is right after all of the left stuff was removed

    for song in left:
        if song not in right:
            leftUniq.append(song)
        else:
            right.remove(song)

    return (leftUniq,right)


def diff(path1 = testpath2,path2 = testpath):
    smaller = pickle.load(open(path1, 'rb'))
    bigger = pickle.load(open(path2, 'rb'))

    print len(smaller),len(bigger)
    delta = []
    for path in bigger:
        if path not in smaller:
            delta.append( (path, ( [],bigger[path] ) ) )
        elif smaller[path] != bigger[path]:
            delta.append((path, songDiff(smaller[path],bigger[path])))

    return delta

if __name__ == "__main__":

    if len(sys.argv) > 1:
        diff(sys.argv[1])
    else:
        diff(FILEPATH)



