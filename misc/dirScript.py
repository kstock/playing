import os
#import sys
from pybloomfilter import BloomFilter
import shutil

ASUS_FILEPATH = "/home/kstock/Music/"
MAC_FILEPATH = "/home/kstock/Music/"

MAC_SAVEPATH = "~/musicToTransfer"

# find . -name "*.mp3" | wc -l
# ==> 21530, rounding up for safety
NUM_ITEMS =  220000
ERROR_RATE = 0.01

def makeData(filepath, bloomname):
    bf = BloomFilter(NUM_ITEMS, ERROR_RATE, bloomname+'.bloom')

    for root,dirs,files in os.walk(filepath):
        #for each file, concat the path directory
        #put all that in the bloom filter
        #print map(lambda f: os.path.join(root,f),files)
        bf.update( map(lambda f: os.path.join(root,f),files) )

    return bf

def songDiff(testInclusionPath,saveDifferencePath,bfPath):

    bf = BloomFilter.open(bfPath)

    for root,dirs,files in os.walk(testInclusionPath):
        for f in map( lambda f: os.path.join(root,f), files):
            if f not in bf:
                print f

                savePath = saveDifferencePath+root

                #TODO possible issue with race condition
                #don't think this is cross platform
                if not os.path.exists(savePath):
                    os.makedirs( savePath )

                shutil.copy2(f,savePath)


if __name__ == "__main__":
    pass

#    if len(sys.argv) > 1:
#        diff(sys.argv[1])
#    else:
#        diff(FILEPATH)



