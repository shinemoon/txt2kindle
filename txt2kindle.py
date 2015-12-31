#!/usr/bin/python
# -*- coding: utf-8 -*-  
# coding: utf-8

import os
import sys

reload(sys)  
sys.setdefaultencoding("utf-8") 


import subprocess
import fsplit.main as fsplit
import fsplit.oswrapper as osw
import re
import shutil


#chapter reg exp
h2re = re.compile(r'\s*第.*章\s*.*')

#chapter list
h2array = []


# lib path
libpath = sys.path[0]

author = "佚名"
title = "N/A"


#Function Define
# Read and handle line by line
def toHtml(fname):
    pass


#Txt Spliter
def txtSpliter(tgt, lines=2000):
    print "----------------------------------"
    print "Start Spliting Txt into Segments"
    print "----------------------------------"
    return fsplit.split(tgt)

#Txt Merger
def txtMerger(txtFiles=[]):
    print "----------------------------------"
    print "Start Merging HTML File"
    print "----------------------------------"

    print "... Assemblying head part"

    hstr  = "<!DOCTYPE html>\n"
    hstr  = hstr + "<html lang='en'>\n"
    hstr  = hstr + "<head>\n"
    hstr  = hstr + "<meta http-equiv='content-type' content='text/html; charset=utf-8'>\n"
    hstr  = hstr + "<title>%s</title>\n"%(title)
    hstr  = hstr + "<style>ol{list-style-type:none;}</style>\n"
    hstr  = hstr + "<style>#toc{page-break-before:always;page-break-after:always;}</style>\n"
    hstr  = hstr + "<style>h2 {page-break-before:always;}</style>\n"
    hstr  = hstr + "</head>\n"
    hstr  = hstr + "<body>\n"
    with open("t2k_tmp/head.split.html","w") as outputf:
        outputf.write(hstr)


    print "... Assemblying foot part"
    estr ="</body>\n"
    estr =estr + "</html>\n"
    with open("t2k_tmp/end.split.html","w") as outputf:
        outputf.write(estr)

    print "... Assemblying TOC part"
    estr = '<nav id="toc" epub:type="toc">\n'
    estr = estr+'<ol>\n'
    for i in range(len(h2array)):
	    estr=estr+'<li><a href="#%d">%s</a></li>\n'%(i+1, h2array[i])
    estr=estr+'</ol>\n'
    estr=estr+'</nav>\n'
    with open("t2k_tmp/toc.split.html","w") as outputf:
        outputf.write(estr)

    # Join File!
    fsplit.join()

    # Handle sample
    shutil.copy("%s/cover.png"%(libpath),"t2k_tmp/cover.png")
    with open("%s/sample.opf"%(libpath),"r") as inputf:
        with open("t2k_tmp/%s.opf"%(title),"w") as outputf:
            opfstr=""
            for line in inputf.readlines():
                line = line.replace("[author_input]", author)
                line = line.replace("[title_input]", title)
                opfstr = opfstr + line
            outputf.write(opfstr)

    # Gen
    subprocess.call("kindlegen t2k_tmp/%s.opf"%(title),shell=True)

    # Clean
    try:
        shutil.copy("t2k_tmp/%s.mobi"%(title),"%s.mobi"%(title))
        #shutil.rmtree(osw.pDir()+"/t2k_tmp")
        pass
    except:
        pass

    pass

#Parse and transform
def txtHandle(cnt):
    h2cnt = 0
    for i in range(1, cnt+1):
        #print "%d.split | "%(i),
        print "|",
        fname = "t2k_tmp/%d.split"%(i)
        with open(fname, 'r') as inputf:
            outputf = open(fname+'.shtml', 'w')
            for line in inputf.readlines():
               str = line.decode('gbk','ignore').encode('utf-8')
               if(h2re.match(str)):
                    h2cnt = h2cnt + 1
                    h2array.append(str.strip('\n').strip('\r'))
                    str = "<h2 id='%d'>"%(h2cnt)+str.strip('\n').strip('\r')+"</h2>\n"
               else:
                    str = "<p>"+str.strip('\n').strip('\r')+"</p>"
               outputf.write(str)     
            outputf.close()
    print "\n... TXT Parsing Done"
    return len(h2array)

#Turn Txt Into Html File
def txt2html(tgt):
    print "----------------------------------"
    print "Try to convert txt file into HTML"
    print "----------------------------------"
    # split files into t2k_tmp
    filecnt = txtSpliter(tgt)
    # loop handling 
    chaptercnt = txtHandle(filecnt) 
    print "... Total %d Chapter Detected"%(chaptercnt)
    for i in h2array:
        #print i
        pass
    print "... HTML file generated."
    txtMerger()
    pass


if(len(sys.argv)==1):
    print "Please use : txt2kindle <txt file path> <novel name> <novel author>"
else:
    tgt = sys.argv[1]
    title = sys.argv[2]
    if(len(sys.argv)>3):
       author = sys.argv[3] 
    print "----------------------------------"
    print "Start to Gen Kindle :"
    print "%s"%(tgt)
    print "书名：%s"%(title)
    print "作者：%s"%(author)
    print "----------------------------------"
    txt2html(tgt)
