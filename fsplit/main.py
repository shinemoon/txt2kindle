#!/usr/bin/env python2
# -*- coding: utf-8 -*-  

##
# fsplit # https://github.com/leosartaj/fsplit.git #
# Copyright (c) 2014 Sartaj Singh
# Licensed under the MIT license.
##

"""
Main module
"""

import os
import oswrapper as osw
import tar
import exce
import sys  
import shutil

reload(sys)  
sys.setdefaultencoding("utf-8") 


def split(fName, lines=2000, dest=None):
    """
    Splits a file into parts
    """
    if not osw.fileExists(fName):
        raise OSError('file \'%s\' does not exists' %(fName))
    base = osw.basename(fName)
    if not dest:
        dest = osw.dirname(fName)
    #dirname = base + '.t2k'
    dirname = osw.pDir()+'/t2k_tmp'

    path = osw.getpath(dest, dirname)
    if(os.path.exists(path)):
        shutil.rmtree(path)

    location = osw.cdir(dirname, dest)

    #to avoid chinese wrong code
    # we need to change the read to read lines!

    """
    # OLD CODE
    size = osw.getsize(fName)
    chunk_size = size / num
    inputf = open(fName)
    for cou in range(num):
        filename = str(cou + 1) + '.split'
        path = osw.getpath(location, filename)
        with open(path, 'w') as outputf:
            osw.fwrite(inputf, outputf, chunk_size)
    filename = str(num) + '.split'
    path = osw.getpath(location, filename)
    with open(path, 'a') as outputf:
        left = size - (chunk_size * num)
        osw.fwrite(inputf, outputf, left)
    """

    # NEW CODE
    size = osw.getlines(fName)
    print "... Book has totally %d lines."%(size)
    chunk_size = lines
    num = size/lines
    if(size%lines!=0):
        num = num + 1
    print "... And will be cut into %d pieces in processing."%(num)
    inputf = open(fName)
    for cou in range(num):
        filename = str(cou + 1) + '.split'
        path = osw.getpath(location, filename)
        with open(path, 'w') as outputf:
            osw.flwrite(inputf, outputf, chunk_size)
    filename = str(num) + '.split'
    path = osw.getpath(location, filename)
    with open(path, 'a') as outputf:
        left = size - (chunk_size * num)
        osw.flwrite(inputf, outputf, left)
    inputf.close()
    return num

def join():
    """
    Joins all the .split.shtml files together systematically
    """
    outputf = open(osw.pDir() +"/t2k_tmp/combined.html", 'w')
    with open(osw.pDir() +"/t2k_tmp/head.split.html") as inputf:
        osw.fwrite(inputf, outputf)

    with open(osw.pDir() +"/t2k_tmp/toc.split.html") as inputf:
        osw.fwrite(inputf, outputf)


    for part in osw.hlistdir():
        partpath = osw.pDir() +"/t2k_tmp/"+ part
        with open(partpath) as inputf:
            osw.fwrite(inputf, outputf)

    with open(osw.pDir() +"/t2k_tmp/end.split.html") as inputf:
        osw.fwrite(inputf, outputf)

    outputf.close()
