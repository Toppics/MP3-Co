# -*- coding: utf-8 -*-
"""
Created on Wed May 11 22:07:17 2022

@author: yan-s
"""

import os
import shutil
from mutagen.easyid3 import EasyID3

path = input(r'Path to dir: ').replace("'", "")
unknown, strange = int(0), int(0)
for (dirpath, dirnames, fileNames) in os.walk(path, topdown=True):
    dirnames[:] = [d for d in dirnames if d not in ['unknownDir','unknownFiles']]    #Block walk in unkowDir
    for file in fileNames:
        fileName = os.path.splitext(file)[0]
        if os.path.splitext(file)[1] == '.mp3':
            if fileName.find(' - ') !=-1:
                try:
                    song = fileName[:fileName.find(' - ')]
                    author = fileName[fileName.find(' - '):].replace(' - ', '')
                    
                    tags = EasyID3(dirpath+'/'+file)
                    tags['title'] = song
                    tags['artist'] = author
                    tags.save()
                    
                    newFile = song+fileName[fileName.find(' - '):]+os.path.splitext(file)[1]
                    os.renames(dirpath+'/'+file, dirpath+'/'+newFile)
                except:
                    strange +=1
                    if not os.path.exists(path+'/unknownFiles'):
                            os.mkdir(path+'/unknownFiles')
                    shutil.move(dirpath+'/'+file, path+'/unknownFiles')
            else:
                unknown +=1
                if not os.path.exists(path+'/unknownDir'):
                        os.mkdir(path+'/unknownDir')
                shutil.move(dirpath+'/'+file, path+'/unknownDir')
print('Number of unknown file :',unknown)
print('Number of strange file :',strange)