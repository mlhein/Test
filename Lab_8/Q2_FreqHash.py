
def getWord(file):
    gWord = file.read()
    gWord = gWord.split()
    return gWord

def countDict(gWord):
    di = dict()
    for w in gWord:
        if w in di:
            di[w] = di[w] + 1
        else:
            di[w] = 1
    for key, value in sorted(di.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: %s" % (key, value)
    return di

if __name__ == "__main__":
    fo = open("input.txt")
    myWords = getWord(fo)
    countDict(myWords)
