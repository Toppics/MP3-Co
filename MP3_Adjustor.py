# -*- coding: utf-8 -*-
"""
Created on Thu May 12 15:51:25 2022

@author: yan-s
"""

import os
import shutil

path = input(r'Path to dir: ').replace("'", "")

for (dirpath, dirnames, fileNames) in os.walk(path):
    for file in fileNames:
        fileName = os.path.splitext(file)[0]
        if os.path.splitext(file)[1] == '.mp3':
            pass
            """
            alias = 'y2meta.com - ' #delete alias at the start of fileName
            if fileName.find(alias) !=-1:
                newFile = fileName[:fileName.find(alias)]+fileName[fileName.find(alias):].replace(alias, '')+os.path.splitext(file)[1]
                os.renames(dirpath+'/'+file, dirpath+'/'+newFile)
            """
            
            '''Add something between fileName and .mp3
            if fileName.find('') !=-1:
                
                newFile = fileName+' - Thérapie Taxi'+os.path.splitext(file)[1]
                os.renames(dirpath+'/'+file, dirpath+'/'+newFile)
            '''

            author = 'Pomme'
            authLen = len(author)
            if fileName.find(author) !=-1:
                newFile = fileName[fileName.find(author):]+ ' - '+ fileName[:fileName.find(author)].replace(' - ', '')+ os.path.splitext(file)[1]
                print(fileName[authLen:],'n')
                print(fileName[fileName.find('Pomme'):])
                #os.renames(dirpath+'/'+file, dirpath+'/'+newFile)
            
        else:
            if not os.path.exists(path+'/unknownFiles'):
                    os.mkdir(path+'/unknownFiles')
            shutil.move(dirpath+'/'+file, path+'/unknownFiles')
            