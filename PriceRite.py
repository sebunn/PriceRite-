##############################################################################
# PriceRite  - test theory as to proper strategy for door picking
#              as in the television game show
#
# by:  Steven Bunn
##############################################################################
from random import randint

import wx
import wxFBfile


# define Classes and Functions
class MainGui(wxFBfile.wxFBclass):
    def __init__(self, parent):
        wxFBfile.wxFBclass.__init__(self,parent)
    #process door choice by override

    def doorOneClick( self, event ):
        processChoice(0)
    def doorTwoClick( self, event ):
        processChoice(1)
    def doorThreeClick( self, event ):
        processChoice(2)

    def tryAgainClick( self, event ):
        newGame()

    def setTriesLabel(self, t):
        self.TriesLabel.LabelText= "Tries : "+ str(t)

    def setWonLabel(self,w):
        self.WonLabel.LabelText= "Won : " + str(w)

    def setPercent(self,p):
        self.Percent.LabelText= str(p)+ " %"

    def showStats(self, w, t):
        if tries==0 : p=0
        else : p= w*100/t
        self.setTriesLabel(t)
        self.setWonLabel(w)
        self.setPercent(p)

    def setDoorCaption(self, d, text):
        if   d == 0: self.DoorOne.LabelText=text
        elif d == 1: self.DoorTwo.LabelText=text
        elif d == 2: self.DoorThree.LabelText=text
        else: pass

    def enableTryAgain(self, b):
        self.TryAgainButton.Enabled=b

    def enableDoors(self, b):
        self.DoorOne.Enabled=b
        self.DoorTwo.Enabled=b
        self.DoorThree.Enabled=b


# define global functions
def processChoice(d):
    global doorsRemain, wins, tries, chosenDoor, prizeDoor

    doorsRemain-= 1
    if doorsRemain == 2:   # Initial choice
        frame.setDoorCaption(d, "Keep this choice?")
        chosenDoor=d
        o1 =d+1                     # 1st Other door
        if o1==3 : o1=0
        o2= o1+1                    # 2nd other door
        if o2 ==3 : o2=0
        if d != prizeDoor :          #either o1 or o2 is the prizeDoor, choose other as hint door
            if o1 ==prizeDoor :
                frame.setDoorCaption(o2, "HINT: not me!")
                frame.setDoorCaption(o1, "Switch to me?")
            else :
                frame.setDoorCaption(o1, "HINT: not me!")
                frame.setDoorCaption(o2, "Switch to me?")
        else :                       # neither o1 or o2 is prize, randomly pick o1 or o2 to show as hint
            if randint(0,1) ==1 :
                frame.setDoorCaption(o2, "HINT: not me!")
                frame.setDoorCaption(o1, "Switch to me?")
            else :
                frame.setDoorCaption(o2, "HINT: not me!")
                frame.setDoorCaption(o1, "Switch to me?")
    elif d == prizeDoor:   # Final choice and is correct
        frame.setDoorCaption(d, "YOU WIN!")
        wins+=1
        tries+=1
        frame.showStats(wins,tries)
        frame.enableTryAgain(True)
        frame.enableDoors(False)
    else :                  # Final choice and is wrong
        frame.setDoorCaption(d, "WRONG DOOR")
        tries+=1
        frame.showStats(wins,tries)
        frame.enableTryAgain(True)
        frame.enableDoors(False)

def newGame():
    global chosenDoor, prizeDoor, doorsRemain

    chosenDoor=-1
    prizeDoor= randint(0,2)
    doorsRemain=3
    frame.enableDoors(True)
    for i in range(0,3): frame.setDoorCaption(i,"Choose me!")
    frame.enableDoors(True)
    frame.enableTryAgain(False)



app = wx.App(False)
frame =MainGui(None)

wins=0
tries=0
frame.showStats(wins, tries)
doorsRemain=3


newGame()
frame.Show(True)
app.MainLoop()

