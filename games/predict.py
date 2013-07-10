from __future__ import division
from collections import defaultdict
from random import choice
import re

COMPUTER = 0
PLAYER   = 1

def notAllZero(iterable):
    for i in iterable:
        if i != 0:
            return True
    return False


class Predict:

    def __init__(self,alphabet = None, winningScore = None,lookbehind = None):
        self.history = ""

        if not alphabet: #else given as a sting already
            print "what do you want the alphabet to be? type the characters"
            alphabet = raw_input()

        self.search=re.compile(r'[^'+alphabet+']').search
        self.alphabet = list( alphabet )

        #used to make sure incorrect char not given by user

        self.index = {}
        for i,elem in enumerate(self.alphabet):
            self.index[elem] = i

        self.freqs = defaultdict(lambda :[0]*len(alphabet))


        if not winningScore:
            print "What score do you want to play to?"
            self.winningScore = int( raw_input() ) #TODO stupid input validation
        else:
            self.winningScore = winningScore

        if not lookbehind:
            print "What int amount of memory should I have"
            self.lookbehind = int( raw_input() ) #TODO stupid input validation
        else:

            self.lookbehind = lookbehind

    def decideAction(self,playerChoice):

        if len(self.history) <= self.lookbehind:
            compChoice = choice(self.alphabet)
        else:
            lastFew       = self.history[-self.lookbehind:]
            pastExperience = self.freqs[lastFew]

            indexOfMax = max((v,i) for i,v in enumerate(pastExperience))[1]

            if  notAllZero(pastExperience): #make sure does random if never seen
                compChoice = self.alphabet[ indexOfMax ]
            else:
                print "random"
                compChoice = choice(self.alphabet)

            #increase the tally for the amount of time playerChoice
            #appeared after the last 4 characters in the history
            mostLikely =  self.index[playerChoice]
            self.freqs[lastFew][mostLikely] += 1

        self.history += playerChoice
        return compChoice

    #search should be function that defines a match. e.g regex
    def special_match(self,strg,search):
        return not bool(search(strg))

        #check if it has illegal characters
#        if  self.special_match(myRandStr,self.search):
            #print "you gave illegal characters. I win by default"
            #return

    def play(self,myRandStr):
        scoreComp = 0
        scorePlayer = 0

        for playerChoice in myRandStr:
            compChoice = self.decideAction(playerChoice)

            print "player == "+str(playerChoice) + " comp =  " + str(compChoice)
            winner = self.whoWinsRound(compChoice,playerChoice)
            if  COMPUTER == winner:
                scoreComp += 1
            else:
                scorePlayer += 1

        print "My score is: " + str(scoreComp) + ",   Your score is: " + str(scorePlayer)
        self.gameOver(scorePlayer,scoreComp)
        self.findProbs(self.history)
        self.reset()

    def whoWinsRound(self,compChoice,playerChoice):
        if compChoice == playerChoice:
            return COMPUTER
        else:
            return PLAYER

    def playAtOnce(self):

        print "Type a random string. I'll look at it character by character and make guesses"
        myRandStr = raw_input()
        self.play(myRandStr)

    def againstPython(self,rounds = 10):
        myRandStr = ''.join( choice(self.alphabet) for strg in xrange(rounds))
        self.play(myRandStr)

    def playInteractive(self, winningScore = 10):

        if winningScore == None:
            winningScore = self.winningScore

        scoreComp = 0
        scorePlayer = 0
        winner = None
        while scoreComp < winningScore and scorePlayer < winningScore:
            print "\n\n\n\n"
            print "------------------------------------------------------"

            if  COMPUTER == winner:
                print "I guessed correct! A point for me!"
                scoreComp += 1
            elif PLAYER == winner: #not blank else to prevent saying on first round
                print "err... You fooled me this time! A point for you!"
                scorePlayer += 1

            print "My score is: " + str(scoreComp) + ",   Your score is: " + str(scorePlayer)
            print "type one of  "+str(self.alphabet)+",I will predict what you will type."
            print "The following is the history, make the next character random!"
            print self.history

            playerChoice = raw_input()

            if playerChoice not in self.alphabet:
                print "\n\n\n\n"
                print "------------------------------------------------------"
                print "No fair! you can only type stuff in "+str(self.alphabet)+"try again!"
                print "------------------------------------------------------"
                continue

            compChoice = self.decideAction(playerChoice)

            winner = self.whoWinsRound(compChoice,playerChoice)

        self.gameOver(scorePlayer,scoreComp)
        self.findProbs(self.history)
        self.reset()

    def findProbs(self,history):

        print "here is my brain: "
        print self.freqs

        print "here is some analysis of your 'randomness'"
        n = len(history)
        freqs = defaultdict(lambda : 0)
        for elem in history:
            freqs[elem] += 1

        for char,numOccurs in freqs.iteritems():
            print char + " occurred with probability: " + str(numOccurs/n)


    def setAlphabet(self):
        alphabet = raw_input()
        self.search=re.compile(r'[^'+alphabet+']').search
        self.alphabet = list( alphabet )
        self.freqs = defaultdict(lambda :[0]*len(alphabet))

        for i,elem in enumerate(self.alphabet):
            self.index[elem] = i

        print "the alphabet is now " + alphabet

    def setLookbehind(self):
       print "What int amount of memory should I have"
       self.lookbehind = int( raw_input() )



    def reset(self):
        self.freqs = defaultdict(lambda :[0]*len(self.alphabet))
        self.history = ""

    def gameOver(self,scorePlayer,scoreComp):
        #game ended
        if scorePlayer == scoreComp:
            print "oy, a tie!"
        elif scorePlayer > scoreComp:
            print "Congratulations! You won!"
        else:
            print "HAHAHAHAHAH I won! Silly deterministic machine!"

