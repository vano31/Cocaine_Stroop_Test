from psychopy import core, visual, gui, data, event
from psychopy.tools.filetools import fromFile, toFile
import numpy, random, csv

expInfo = {'Last Name': ' ', 'First Name':' '} ###Change to subject id
expInfo['dateStr'] = data.getDateStr()

#present a dialogue to change params
dlg = gui.DlgFromDict(expInfo, title='Cocaine Study Stroop Test', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo) #save params to file for next time
else:
    core.quit() #the user hit cancel, so exit
    
#make a csv file to store the data
fileName = expInfo['Last Name'] + '_' + expInfo['First Name'] + 'CocaineStroopTest' + expInfo['dateStr']
dataFile = open(fileName + '.csv', 'w') # a simple text file with comma seperated values
dataFile.write('blocks,thisN,thisRepN,word,type,number,answer,key_pressed,correct,time_button_pressed,time_fixation_cross_appeared,time_fixation_cross_stopped,duration_fixation_cross,time_word_appeared,time_word_stopped,duration_word,\n')

#import main.xlsx
mainlist = data.importConditions('main.xlsx')

#get pre-seq prior from mainlist (needs to be pre because personal words will be inserted later once personal word number is determined to either be set or random)
preseq1_1 = mainlist[0]
preseq1_2_ic = mainlist[1]
preseq1_3 = mainlist[2]

preseq2_1 = mainlist[3]
preseq2_2_ic = mainlist[4]
preseq2_3 = mainlist[5]

preseq3_1 = mainlist[6]
preseq3_2_ic = mainlist[7]
preseq3_3 = mainlist[8]

####################################################################################################
'''
Step 1. Load personal_words_randomization.xlsx.
    - if personal_word_randomization is "none", then proceed
Step 2. Load list_of_twelve_personal_words.xlsx twice into a 2d list. list[0] contains the list random


Everything below this line is no longer necessary because randomization only occurs once per participant, the number of times the personalized words appear in
a frame is fixed, personal word slots are fixed, and the list of 12 words must be randomized, then inserted into slots, then 12 words are randomized again, and
then inserted into remaining slots.
'''
####################################################################################################


#import personal_words_order_and_number.xlsx
personal_words = data.importConditions('personal_words/personal_words_order_and_number.xlsx')

#get personal_word_order value from mainlist to determine if word order is set or random
random_or_set_order = mainlist[9]["personal_word_number"]


#Do this if random_or_set_order is set to random. Will randomize the personal words dict list prior to insertion
if random_or_set_order == "random":
    l = len(personal_words)
    newlist = l * [0]
    
    for x in range(0,len(newlist)):
        rand_integer = random.randrange(0,l)
        newlist[x] = personal_words[rand_integer]
        personal_words.pop(rand_integer)
        l -= 1
        
    personal_words = newlist

def personal_word_number_randomizer(preseqlist):
    for i in range(0,len(preseqlist)):
        if preseqlist[i]["type"] == "personal":
            randnumber = random.randrange(1,5)
            preseqlist[i]["number"] = randnumber
            preseqlist[i]["answer"] = f"{randnumber+1}"

def personal_word_inserter(preseq):
    preseqlist = data.importConditions(preseq["blocks"])
    for i in range(0,len(preseqlist)):
        if preseqlist[i]["word"] == "":
            preseqlist[i] = personal_words.pop(0)
    if preseq["personal_word_number"] == "random":
        personal_word_number_randomizer(preseqlist)
    return preseqlist
    
seq1_1 = data.TrialHandler(trialList=personal_word_inserter(preseq1_1),nReps=1,method='sequential',originPath=None)
seq1_2_ic = data.TrialHandler(trialList=personal_word_inserter(preseq1_2_ic),nReps=1,method='sequential',originPath=None)
seq1_3 = data.TrialHandler(trialList=personal_word_inserter(preseq1_3),nReps=1,method='sequential',originPath=None)
    
seq2_1 = data.TrialHandler(trialList=personal_word_inserter(preseq2_1),nReps=1,method='sequential',originPath=None)
seq2_2_ic = data.TrialHandler(trialList=personal_word_inserter(preseq2_2_ic),nReps=1,method='sequential',originPath=None)
seq2_3 = data.TrialHandler(trialList=personal_word_inserter(preseq2_3),nReps=1,method='sequential',originPath=None)

seq3_1 = data.TrialHandler(trialList=personal_word_inserter(preseq3_1),nReps=1,method='sequential',originPath=None)
seq3_2_ic = data.TrialHandler(trialList=personal_word_inserter(preseq3_2_ic),nReps=1,method='sequential',originPath=None)
seq3_3 = data.TrialHandler(trialList=personal_word_inserter(preseq3_3),nReps=1,method='sequential',originPath=None)


win = visual.Window(fullscr=True,allowGUI=True, checkTiming=True)
welcome_message = visual.TextStim(win, pos=[0,0], text='Welcome to the Stroop Test! Press t to continue.')
#fixation_cross = visual.Fixa
instruction_1_text = 'In this task you will count the number of words you see on the screen' + '\n' + 'Then press the button as fast as you can to indicate the number of words you counted.' + '\n' + 'Let\'s practice! Press BUTTON 1 (index finger) now'


#the seqx_x need to have the number and answers blank for the personal words in case you want those words to appear a certain amount randomly
'''
image | duration | button press duration |

welcome_screen = 

for increment in sequence:
    run the fixation for certain amount of frames
    run increment for certain amount of frames
        display correct number of words on screen
        record key presses and other data
        record the frame at which buttons was pressed, convert that to milliseconds, and record
        
after increment in sequence, then implement planned pauses according to frames

'''


