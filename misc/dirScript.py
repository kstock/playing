import os,pickle
from pybloom import BloomFilter
import shutil

ASUS_FILEPATH = "/home/kstock/Music/"
MAC_FILEPATH = "/home/kstock/Music/"

MAC_SAVEPATH = "~/musicToTransfer"

# find . -name "*.mp3" | wc -l
# ==> 21530, rounding up for safety
NUM_ITEMS =  240000
ERROR_RATE = 0.01

def makeData(filepath, bloomname):
    bf = BloomFilter(capacity=NUM_ITEMS, error_rate=ERROR_RATE)

    for root,dirs,files in os.walk(filepath):
        #for each file, concat the path directory
        #put all that in the bloom filter
        #print map(lambda f: os.path.join(root,f),files)
        for fixed in  map(lambda f: os.path.join(root,f),files):
            #turns out ubuntu files have a dash in them
            #mac ones don't
            bf.add(fixed.replace(" -",""))

    pickle.dump(bf,open(bloomname,'wb'))

def songDiff(testInclusionPath,saveDifferencePath,bfPath):

    bf = pickle.load(open(bfPath,'rb'))

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
