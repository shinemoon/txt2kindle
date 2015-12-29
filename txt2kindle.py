#!/usr/bin/python
import os
import sys
import subprocess

#kindlegen path
kindlegen = "/Users/iclaud/Nutstore/tool/kindlegen/KindleGen_Mac_i386_v2_9/kindlegen"


if(len(sys.argv)==1):
    print "Please use : txt2kindle <txt file path> "
else:
    tgt = sys.argv[1]
    print "Gen %s"%(tgt)





