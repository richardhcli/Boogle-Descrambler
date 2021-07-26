print('Boggle descrambler by Richard and Dad')


Lowest_wordlength_kept = 7 #must be greater or eqaal to  7
                            # too small will generate to much


pathto_wordlist = r"C:\Users\joyri\Desktop\python_stuffs\Boggledescrambler\alldictionary.txt"
import os
import sys
import numpy as np
import time
from tkinter import *
start = time.time()

#myfolder=r'C:\Users\joyri\Desktop\python stuffs\Boggledescrambler'

##
##
##myfolder=r"C:\Users\joyri\Desktop\python_stuffs\Boggledescrambler"
##
###writefilename=myfolder+'\Boggledescrambler_wordfound.txt'   
##
###finding dic(phase1)start
##
##def load_words(fullname):  #checks if is correct and OUTPUTS SET OF WORDS
##    name = os.path.splitext(os.path.basename(fullname))[0]
##    #print(name)
##    if name!= '2of12inf(USE)' and name!='3of6all(USE)' and name!='3of6game(USE)' \
##       and name!='5d+2a(obsurewords)' and name!='dictionary2 - Copy(USE)' and \
##       name!='words_alpha' and name!='2of4brif' and name!='2of12' and name!='3esl'\
##       and name!='6of12':
##        print(name + ' is not in the dictionary')
##        sys.exit()
##    with open(fullname) as word_file:
##        valid_words = set(word_file.read().split())
##    return valid_words
##
##
##set1=load_words(myfolder+r'\2of12inf(USE).txt')
##set2=load_words(myfolder+r'\3of6all(USE).txt')
##set3=load_words(myfolder+r'\3of6game(USE).txt')
##set4=load_words(myfolder+r'\5d+2a(obsurewords).txt')
##set5=load_words(myfolder+r'\dictionary2 - Copy(USE).txt')
##set6=load_words(myfolder+r'\words_alpha.txt')  #biggest file(suspicious)
###next dics, might not use
##set7=load_words(myfolder+r'\2of4brif.txt')
##set8=load_words(myfolder+r'\2of12.txt')
##set9=load_words(myfolder+r'\3esl.txt')
##set10=load_words(myfolder+r'\6of12.txt')
###del 
##
##
##
##allset = set1.union(set2, set3, set4, set5,set6,set7,set8,set9,set10)
###allset = set1.union(set2, set3, set4, set5,set7,set8,set9,set10)

with open(pathto_wordlist) as word_file:
    allset = set(word_file.read().split())

#t='banana'
#if t in allset:
#    print('word %s is in allset'%(t))
#dictionary complete        -----------------------------------------
#phase 2: create matrix and input letters

##print('Matrix =\n')
##global m
###Week 1
###m=[['m', 'e','n','r'],['u','q','a','t'],['g','r','u','n'],['i','t','s','i']]
###Week 2
###m=[['h', 'w','r','i'],['s','o','z','o'],['e','p','o','s'],['d','e','c','n']]    
###week 3
###m=[['m', 'e','a','k'],['g','r','b','f'],['n','r','u','a'],['i','t','s','l']]
###week 4
###m=[['t', 's','i','x'],['p','a','l','t'],['g','u','r','t'],['q','h','e','i']]
###week 5
###m=[['h', 'g','i','e'],['t','e','x','t'],['e','r','a','n'],['d','n','g','d']]
###input m is at bottom of phase 3
###phase 3: check if words in dictionary can be generated

def nextpos(r,c):
    allpos=[] #all future posible positions
    global nR, nC
    if r<0 or r>nR or c<0 or c>nC:
        print('({},{}) is not valid position '.format(r,c))
        sys.exit()

    #senario 1 same row, diff col
    if c-1>=0:
        allpos.append([r,c-1])
    if c+1<nC: #not <= because starts from zero, nC counts 0 as 1
        allpos.append([r,c+1])

    #senario 2 row-1, all neighboring col
    if r-1>=0:
        allpos.append([r-1,c])
        if c-1>=0:
            allpos.append([r-1,c-1])
        if c+1<nC:
            allpos.append([r-1,c+1])

    #senario 3 row+1, all neighboring col
    if r+1<nR:
        allpos.append([r+1,c])
        if c-1>=0:
            allpos.append([r+1,c-1])
        if c+1<nC:
            allpos.append([r+1,c+1])
    return allpos
                
#print(nextpos(3,1)) #test



def locateletter(thisletter):   #two for statements in one
    global m
    pos=[(ix,iy) for ix, row in enumerate(m) for iy, i in enumerate(row) if i ==thisletter]
    return pos
#enumerate returns position and value;very useful

#test
##print(locateletter('w'))

def one_word_tracing(W):  # sees if input word and be traced from matrix
    global m
    W1=''
    for k in range(0,len(W)): #gets rid of weird symbols
        if not W[k] in [':', '$','!','+','~','=',"'",'<','>','#']:
            W1 = W1+W[k]
    W=W1

            
    len_W=len(W)
    for k in range(0,len_W):
         
         pos=locateletter(W[k])
    #     print(pos) 
         if k>0:    # not first letter
             if W[k] not in Nextpos_letters:  # in previous next pos list
                 Done=False  
                 break 
             elif k==len_W-1: # last letter is found
                 Done=True
                 break
    #             return True
                 
             else:        # found but not last letter
                 Nextpos=[] 
                 for loc in range(0, len(pos)):  # loop the pos: but cannot take non-neighboring pos
                     thispos=pos[loc]
                     ### compare to previous pos, discard if not next to
                     if thispos not in pre_Nextpos:
                         continue # skip due to nonneighboring same letter
                     ### compare to previous pos, discard if not next to
    #                 print(thispos)
                     Nextpos+=nextpos(thispos[0],thispos[1])
                    #removing duplicate sublist using set() + sorted()  
                 Nextpos = list(set(tuple(sub) for sub in Nextpos)) 
                 Nextpos_letters=[m[pos1[0]][pos1[1]]  for pos1 in Nextpos]  
                 
                 pre_Nextpos=Nextpos.copy()
             
         else: # k==0, first letter
            if len(pos)==0:   # does not find
                Done=False  
                break
    #            return False
    #            break
            elif len_W==1:  # found and the word has only one letter
                Done=True  
                
            else:  # found but longer than 1
                 Nextpos=[]   
                 for loc in range(0, len(pos)):  # loop the pos: only the first time can use more than two non adjacent pos
                     thispos=pos[loc]
                     Nextpos+=nextpos(thispos[0],thispos[1])
                    #removing duplicate sublist using set()  #cannot sort!
                 Nextpos = list(set(tuple(sub) for sub in Nextpos)) 
                 Nextpos_letters=[m[pos1[0]][pos1[1]]  for pos1 in Nextpos]  
                 pre_Nextpos=Nextpos.copy()
                 #copy() allows Nextpos to change but pre_Nextpos to not change for different python versions
    
    return Done
    



print('--------------------------------------------')






#inp = input('input string of 16 letters to be an array ')
#while len(inp) != 16:
#    print('not a four by four grid, try again')
#    inp = str(input('input string of 16 letters to be an array '))


global nR, nC

def entire_program():        
    global nR, nC,m,tk
    nR=len(m)
    nC=len(m[0])
    #both 4
    #nR and nC are the size of matrix
    #r and c are current position
    array =np.full((4,4),m)
    print(array)  #nice visual
    Label(tk,text=array).pack()

    longest_word = []
    long_words = []
    for word in allset:
        word_test = one_word_tracing(word)
        if word_test == True and len(word) > Lowest_wordlength_kept:
            long_words.append(word)
        if  word_test == True and len(word) > len(longest_word):
            longest_word = word
            
        

    ordered_long_words = sorted(long_words, key=len)
    print('%s words with length longer than %s:\n'%(len(long_words), Lowest_wordlength_kept))

    for i in ordered_long_words:
          print(i,len(i))
          Label(tk, text=[i,len(i)]).pack()
    

    print('The longest word is %s with a length of %s'%(longest_word, len(longest_word)))
    Label(tk,text='The longest word is %s with a length of %s'%(longest_word, len(longest_word))).pack()
    

    ##
    ###write to txt file
    ####with open("outfile", "w") as outfile:
    ####    outfile.write("\n".join(itemlist))
    ##file1 = open(writefilename,"w")
    ##file1.write('Max word length=%s;   %s words are found in %s seconds!\n'\
    ##            %(len_word,len(lword),end - start))
    ##file1.write("\n".join(lword))
    ##file1.close() 





    global loops,startnext
    end = time.time()
    if loops == 0:
        print('It took %s seconds.\n'%(round(end - start,3)))
        loops+=1
        Label(tk,text='It took %s seconds.\n'%(round(end - start,3))).pack()
    else:
        print('It took %a seconds. \n'%(round(end-startnext,3)))
        Label(tk,text='It took %s seconds.\n'%(round(end - startnext,3))).pack()




def turnintolist(playerinput):
    allvar=[]
    for repeat in range(0,4):
        temp = []
        for x in range(0,4):
            if x+(repeat*4) < 16:
                temp.append(playerinput[x+(repeat*4)])
                #print(x+(repeat*4))
        #print(temp)
        allvar.append(temp)
    return allvar

def all_children(window) :
    _list = window.winfo_children()
    return _list
        

    
global playerinput
global loops
loops = 0

def func(event):
    global m, loops,startnext
    startnext = time.time()
    
    
    widget_list = all_children(tk)
    for item in widget_list:
        if item == playerin or item == question or item == templabel:
            continue
        else:
            item.pack_forget()
    
    print('input: %s'%(question.get()))
    if len(question.get()) != 16:
        templabel.configure(templabel, \
            text='input: {0}, you put in a word of length {1}, words need to be 16 digits long '\
                            .format(question.get(),len(question.get())))

                                    
    

    else:
        templabel.configure(templabel, text='Good')
        
        playerinput = str(question.get())
        m = turnintolist(playerinput)
        entire_program()
        
global tk
tk = Tk()
tk.title('Created by Richard Li')

playerin = Label(tk, text="Boogle descrambler made by Richard\n\
this process will take around 15 seconds, lowest length=7\n\
please input 16 letters to be an array")
playerin.pack()
#playerin.tag_add(

question = Entry(tk)
question.pack()

templabel = Label(tk)
templabel.pack()

question.bind("<Return>", func)
tk.mainloop()





