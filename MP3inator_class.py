# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:55:49 2022

@author: yan-s
"""
#import modules
from os import scandir, listdir, makedirs
from shutil import copy

class MP3inator():    
    def __init__(self, biblioPath = 'D:\Musique\Y-S'):
        "Init path and list"
        #Path to library
        self.biblioPath = biblioPath
        #Path to src directory
        self.exist('Path to src directory : ')
        
        #Init exeLog
        self.exeLog =[]
        #Prepare round TWo
        self.roundTwo =[]
        #Init duplicateVar
        self.duplicateVar = 0
        #Choose if show execution print sequence
        self.printf = False
        #Define lists yes and no
        self.yes =['Y', 'YES', 'O', 'OUI']
        self.no =['N', 'NO', 'NON']
        
        #Ask user if want the print of the prog 
        while True:
            quitt = input('Print execution sequence (y/n) ? ')
            if quitt.upper() in self.yes:
                self.printf = True
                break
            if quitt.upper() in self.no: break
            print("Please enter 'y' or 'n'")
            
        #Define list of may-cause-things-to-fail
        self.replaceList = ['' , 
                       '.mp3', '.m4a', '.webm',
                       '...', '..', '.', ',',
                       '(', ')', '[', ']',
                       '-', '_', '"', "'",
                       'official', 'officiel', 'original',
                       'audio', 'soundtrack', 'track',
                       'with lyrics', 'lyrics',
                       'video', 'clip',
                       'complete', 'version',
                       'quality', 'hd', 'hq']
        
    def exist(self, arg):
        "Check if directory exist"
        while True:
            self.path = input(arg).replace("'", '')
            try:
                scandir(self.path)
                return
            except FileNotFoundError:
                print('\nError, this directory doesn\'t exist ! Try again. ', end='')
        
    def print_(self, arg):
        "Print and add to log list"
        #Print the input gave
        print(arg)  
        #Add to log list the input gave
        self.exeLog.append(arg)        
        
    def preFile(self, file):
        "Prepare file name"
        #Lower file
        file = file.lower()
        #for every element in replaceList
        for element in range(0, (int(len(self.replaceList))-1)):
            #if 'element' in replaceList, remove it ('')
            if file.find(self.replaceList[element+1]):
                file = file.replace(self.replaceList[element+1], self.replaceList[0])
        #if double space find, replace with only one
        if file.find('  '):
            file = file.replace('  ', ' ')
        #if extra-space at the end, remove it
        if file.endswith(' '):
            file = file[:-1]
        #Return file
        return file
    
    def loadList(self):
        "Load all the Music from biblio in two list, 1st with real name, 2nd with work name : we need the position in list of the 2nd to return the 1st"
        self.biblio = []     #List with the real name of file
        self.wBiblio = []    #List of list of the word in the name of file
        #for every music in src directory
        for music in listdir(self.biblioPath):
            """ Vérifier si bien un fichier audio """
            #Add all music files to biblio
            self.biblio.append(music)
            #Add all 'word list' of music files to wBiblio
            self.wBiblio.append((self.preFile(music)).split(' '))
        #Show when done
        self.print_('\n--Biblio load !\n')
        
    def classification(self):
        "Do the real work :"
        #For words in list file
        for words in self.file:
            #init/reset number of times word found in files counter
            occurence = 0
            #Add to log list 'word' search
            self.exeLog.append(('\n-{0}:').format(words))
            #We need to start at -1, 'cause increment before used
            index = -1
            #For every 'word list' of wBiblio
            for wordsList in self.wBiblio:
                #Increment index of
                index +=1
                #For every 'words' in 'word list' of wBiblio
                if words in wordsList:
                    #Increment number of times word found counter
                    occurence +=1
                    #Add to log list
                    self.exeLog.append(wordsList)
                    self.exeLog.append((index, ':', self.biblio[index]))   
                    #Add index music to foundList
                    self.foundList.append(self.biblio[index])
                
                #If title lenght title src = 85% of title dest
                if (len(self.file)*0.85) <= self.foundList.count(self.biblio[index]):
                    """
                    Should add more classification options
                    (size file, durée...)                
                    """   
                    #Increment the index of duplicate file
                    self.duplicate[self.biblio[index]] = self.duplicate.get(self.biblio[index], 0) +1
                    #make the move
                    self.dest = 'C:\\Users\\ivanr\\Desktop\\Pypi\\cwd\\Output'+'\\'
                    #In case directory is missing
                    try: makedirs(self.dest)
                    except: pass
                    copy((self.biblioPath+'/'+self.biblio[index]), (self.dest+self.biblio[index]))
                    #Rmv the name of the music from unfounds files
                    del self.notFound[-1:]
                    #Print file src and dest
                    if self.printf == True : print('"{0}" --> "{1}"'.format(self.nameFile, self.biblio[index]))
                    #Add to log list 
                    self.exeLog.append(('"{0}" --> "{1}"'.format(self.nameFile, self.biblio[index])))
                    #Stop the loop = only 1 file for 1 file
                    return   
            
            #Add to log list number of times word found in files
            self.exeLog.append(('Occurence du mot "{0}" : {1}').format(words, occurence))
        
    def main(self, exit_ = 0):
        "Do the Work and could be subdivise"
        self.print_('--Starting !\n')
        #Init list and dico
        self.notFound =[]
        self.duplicate ={}
        
        #First round        #For files in directory
        if exit_ == 0: iterable = listdir(self.path)    
        #Second run         #For files unfound
        else: iterable = self.roundTwo
        
        #Split in, count number of 'words' and test in classification
        for file in iterable:
            #foundList init/reset
            self.foundList = []
            #Add to list notFound
            self.notFound.append(file)
            #Var for showing wich became what
            self.nameFile = file
            #Change file name & split in list 
            self.file = (self.preFile(file)).split(' ')
            #Add to log list
            self.exeLog.append(('\nNew file --', 'Nombre de mots : ', len(file)))
            #Launch the real work
            self.classification()                    
           
        #Round done !
        self.print_('\n--Done !')

        #Show unfound files
        if len(self.notFound) != 0:
            #Print number unfound file and names
            self.print_(('\n{0} file(s) not found : {1}\n').format(len(self.notFound), self.notFound))
        else:
            #In a Brave New World
            self.print_('\nAll files found !')   
                
        #Show duplicate move
        for nom in self.duplicate:
            item = self.duplicate[nom]
            #If music transferred more than 1 time 
            #(means that minimum, 2 musics returns the same file)
            if item > 1: 
                #Print number times file moved and it's name                          
                self.print_('-File : "{0}" moved {1} times.'.format(nom, item))
                #Increment number of duplicate file
                self.duplicateVar +=1    
                
        #Print Output directory
        self.print_('\nMusics in directory "%s"' % self.dest)
        
        #Print number of untransferred files + propose 2nd run
        if len(self.notFound) or self.duplicateVar != 0:
            #Print number of untransferred files and types (duplicate/ unfound)
            self.print_('\n{0} files not transferred : {1} not found & {2} duplicate.'.format((len(self.notFound) + self.duplicateVar), len(self.notFound), self.duplicateVar))
            #Check if there is unfound files and it's the 1st run
            if len(self.notFound) != 0 and exit_ == 0:
                #Ask for 2nd run
                while True:
                    quitt = input('\nTry again (could work for some files) (y/n) ? ')
                    if quitt.upper() in self.yes:
                        #Launch 2nd run
                        self.secondChance()
                        break
                    if quitt.upper() in self.no: break
                    print("Please enter 'y' or 'n'")
        
    def secondChance(self):
        "Make a 2nd run with the unfound files and try in a diffrnt way"
        #roundTwo = file unfound in 1st run and search again 
        #in the 2nd run
        self.roundTwo = self.notFound.copy()
        #The real change : replacement caracter '' --> ' '
        self.replaceList[0] = ' '
        #load lists again
        self.loadList()
        #launch main 2nd part (1 could be anything except 0 )
        self.main(1)
        
    def saveExeLog(self):
        "Ask fot saving log in file 'exeLog' encoding utf8"
        #Ask user if want the log file of execution
        while True:
            quitt = input('Save log file (y/n) ? ')
            if quitt.upper() in self.yes:
                #Encoding "ansi" (default 2x lighter), 
                #maybe use it instead of "utf8"
                with open('exeLog', 'w', encoding="Utf8") as log:
                    log.write('---Welcome to debug file---'+'\n' +\
                              'explication / légende...')
                    for ligne in exeSeq.exeLog:
                        #If encoding dont have caracter
                        try:
                            log.write(str(ligne)+'\n')
                        except UnicodeEncodeError:
                            log.write('<invalid caracter>'+'\n')
                #Print path of the log file
                print('\n"exeLog" file in directory "%s"' % self.dest)
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
        
#if run as main   
if __name__ == '__main__':
    #Create object exeSeq
    exeSeq = MP3inator()
    #Execution Sequence
    exeSeq.exeSeq()
    
    
""" # C:\\Users\\ivanr\\Desktop\\Pypi\\cwd\\Input
Prochaine modification :
    -clean up
    -réessayer de réutiliser f° yes_no()
    -ajouter une vérification dans loadList() que file == audio file
    (.mp3, .m4a, .webm ...)
    -ajouter entrée à partir de .txt (read)
    -Should add more classification options (file size, durée...)          
"""