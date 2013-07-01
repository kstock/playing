from collections import defaultdict
from random import choice
import re

COMPUTER = 0
PLAYER   = 1

class Predict:

    def __init__(self,domain = None, goal = None,lookbehind = None):
        self.history = ""


        if not domain: #else given as a sting already
            print "what do you want the domain to be? type the characters"
            domain = raw_input()

        self.search=re.compile(r'[^'+domain+']').search
        self.domain = list( domain )

        #used to make sure incorrect char not given by user

        self.index = {}
        for i,elem in enumerate(self.domain):
            self.index[elem] = i

        self.freqs = defaultdict(lambda :[0]*len(domain))


        if not goal:
            print "What score do you want to play to?"
            self.goal = int( raw_input() ) #TODO stupid input validation
        else:
            self.goal = goal

        if not lookbehind:
            print "What int amount of memory should I have"
            self.lookbehind = int( raw_input() ) #TODO stupid input validation
        else:

            self.lookbehind = lookbehind

    def decideAction(self,playerChoice):

        if len(self.history) <= self.lookbehind:
            compChoice = choice(self.domain)
        else:
            lastFew       = self.history[-self.lookbehind:]
            pastExperience = self.freqs[lastFew]
            print pastExperience

            indexOfMax = max((v,i) for i,v in enumerate(pastExperience))[1]
            print "max index === " + str(indexOfMax)
            if  self.notAllZero(pastExperience): #make sure does random if never seen
                compChoice = self.domain[ indexOfMax ]
            else:
                print "random"
                compChoice = choice(self.domain)

            #increase the tally for the amount of time playerChoice
            #appeared after the last 4 characters in the history
            mostLikely =  self.index[playerChoice]
            self.freqs[lastFew][mostLikely] += 1
            print self.freqs

        self.history += playerChoice
        return compChoice

    #search should be function that defines a match. e.g regex
    def special_match(self,strg,search):
        return not bool(search(strg))

    #TODO check iteration stuff
    def notAllZero(self,iterable):
        for i in iterable:
            if i != 0:
                return True

        return False

    def playAtOnce(self):

        print "Type a random string. I'll look at it character by character and make guesses"
        myRandStr = raw_input()

        #check if it has illegal characters
#        if  self.special_match(myRandStr,self.search):
            #print "you gave illegal characters. I win by default"
            #return

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

#@staticmethod
    def whoWinsRound(self,compChoice,playerChoice):
        if compChoice == playerChoice:
            return COMPUTER
        else:
            return PLAYER



    def playInteractive(self):

        scoreComp = 0
        scorePlayer = 0
        while scoreComp < self.goal and scorePlayer < self.goal:
            print "\n\n\n\n"
            print "------------------------------------------------------"
            print "My score is: " + str(scoreComp) + ",   Your score is: " + str(scorePlayer)
            print "type one of  "+str(self.domain)+",I will predict what you will type."
            print "The following is the history, make the next character random!"
            print self.history

            playerChoice = raw_input()

            if playerChoice not in self.domain:
                print "No fair! you can only type stuff in "+str(self.domain)+"try again!"
                continue

            compChoice = self.decideAction(playerChoice)

            winner = self.whoWinsRound(compChoice,playerChoice)
            if  COMPUTER == winner:
                print "I guessed correct! A point for me!"
                scoreComp += 1
            else:
                print "err... You fooled me this time! A point for you!"
                scorePlayer += 1

        self.gameOver(scorePlayer,scoreComp)

    def gameOver(self,scorePlayer,scoreComp):
        #game ended
        if scorePlayer == scoreComp:
            print "oy, a tie!"
        elif scorePlayer > scoreComp:
            print "Congratulations! You won!"
        else:
            print "HAHAHAHAHAH I won! Silly deterministic machine!"

        self.freqs = defaultdict(lambda :[0]*len(self.domain))
