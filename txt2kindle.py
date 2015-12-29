#!/usr/bin/python
import os
import sys
import subprocess

#kindlegen path
kindlegen = "/Users/iclaud/Nutstore/tool/kindlegen/KindleGen_Mac_i386_v2_9/kindlegen"


#chapter reg exp
chapterana = ""



#Function Define
#Txt Spliter
def txtSpliter(size="500k"):
    print "----------------------------------"
    print "Start Spliting Txt into Segments"
    print "----------------------------------"
    pass

#Txt Merger
def txtMerger(txtFiles=[]):
    print "----------------------------------"
    print "Start Merging HTML File"
    print "----------------------------------"
    pass


#Turn Txt Into Html File
def txt2html():
    print "----------------------------------"
    print "Try to convert txt file into HTML"
    print "----------------------------------"
    txtSpliter()
    txtMerger()
    pass


if(len(sys.argv)==1):
    print "Please use : txt2kindle <txt file path> "
else:
    tgt = sys.argv[1]
    print "----------------------------------"
    print "Start to Gen Kindle :"
    print "%s"%(tgt)
    print "----------------------------------"
    txt2html()
