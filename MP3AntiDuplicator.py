# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 18:01:03 2022

@author: yan-s
"""

import difflib
from os import scandir, listdir
from time import sleep

class MP3AntiDuplicator():    
    def __init__(self):
        "Init path and list"                
        #Path to src directory        
        while True:
            self.path = input('Path to src directory : ').replace("'", '')
            try:
                scandir(self.path)
                break
            except FileNotFoundError:
                print('\nError, this directory doesn\'t exist ! Try again. ', end='')
        # 'C:\Users\yan-s\Music'
        
        #Init exeLog
        self.exeLog =[]
        #Define lists yes and no
        self.yes =['Y', 'YES', 'O', 'OUI']
        self.no =['N', 'NO', 'NON']
        
        #Define list of may-cause-things-to-fail
        self.replaceList = ['' , 
                       '.mp3', '.m4a', '.webm',
                       '...', '..', '.', ',',
                       '(', ')', '[', ']',
                       '-', '_', '"', "'",
                       '&', '!', '?',
                       'official', 'officiel', 'original',
                       'audio', 'soundtrack', 'track',
                       'with lyrics', 'lyrics',
                       'video', 'clip',
                       'complete', 'version',
                       'quality', 'hd', 'hq']
            
    def preFile(self, file):
        "Prepare file name"
        #Lower file
        file = file.lower()
        #for every element in replaceList
        for element in range(0, (int(len(self.replaceList))-1)):
            #if in replaceList, remove it
            if file.find(self.replaceList[element+1]):
                file = file.replace(self.replaceList[element+1], self.replaceList[0])
        #if double space find, replace with only one
        if file.find('  '):
            file = file.replace('  ', ' ')
        #if extra-space at the end, remove it
        if file.endswith(' '):
            file = file[:-1]
        return file
    
    def loadList(self):
        "Load all the Music from biblio"
        self.wBiblio = []
        self.biblio = []
        #for every music in src directory
        for music in listdir(self.path):
            self.wBiblio.append(music)
            self.biblio.append(self.preFile(music))
        
    def main(self, exit_ = 0):
        "Do the Work"
        print('--Starting !\n')        
        index = -1
        for file in self.biblio:
            index +=1
            seq1 = file
            for name in self.biblio:
                seq2 = name
                if self.biblio.index(name) != self.biblio.index(file):
                    if difflib.SequenceMatcher(a=seq1, b=seq2).ratio() > 0.9:
                        self.exeLog.append(self.wBiblio[index])
                        print(self.wBiblio[index])        
                
        # Done !
        print('\n--Done !')
        
    def saveExeLog(self):
        "Ask fot saving log in file 'exeLog' encoding utf8"
        #Ask user if want the log file of execution
        sleep(0.9)
        while True:
            quitt = input('Save log file (y/n) ? ')
            if quitt.upper() in self.yes:
                #Encoding "ansi" (default 2x lighter), 
                #maybe use it instead of "utf8"
                with open('exeLog', 'w', encoding="Utf8") as log:
                    log.write('---Welcome to debug file---'+'\n' +\
                              'explication / légende...'+'\n'*2)
                    for ligne in exeSeq.exeLog:
                        #If encoding dont have caracter
                        try:
                            log.write(str(ligne)+'\n')
                        except UnicodeEncodeError:
                            log.write('<invalid caracter>'+'\n')
                break
            if quitt.upper() in self.no: break
            print("Please enter 'y' or 'n'")
            
    def exeSeq(self):
        "Launch the execution Sequence"
        #Load lists
        self.loadList()
        #Do the work
        self.main()
        #Save log
        self.saveExeLog()
        
        print('\nHave a nice day !')
        

if __name__ == '__main__':
    exeSeq = MP3AntiDuplicator()
    exeSeq.exeSeq()
    