from statenode import StateNode
from prettyformatter import PrettyFormatter
from prettyprinter import PrettyPrinter

class GameState:
    def __init__(self, startNode, textPrintSpeed, imagePrintSpeed):
        self.__currentNode = startNode
        self.__textPrintSpeed = textPrintSpeed
        self.__imagePrintSpeed = imagePrintSpeed

    @property
    def currentNode(self):
        return self.__currentNode

    @property
    def textPrintSpeed(self):
        return self.__textPrintSpeed
    
    @property 
    def imagePrintSpeed(self):
        return self.__imagePrintSpeed

    def changeStateDueToAction(self, actionNumber):
        connections = self.currentNode.connectingStates
        assert(actionNumber >= 0 and actionNumber < len(connections))
        self.__currentNode = connections[actionNumber]

    def printCurrentNode(self):
        print("\n---------------------------------------------------------")
        PrettyPrinter.printLineByLine(self.currentNode.nodeImage, self.imagePrintSpeed)
        if(self.currentNode.nodeImage != ""):
            print("\n---------------------------------------------------------")
        PrettyPrinter.printCharacterByCharacter(self.currentNode.nodeDescriptionText, 100, self.textPrintSpeed)
        print("\n---------------------------------------------------------")
        PrettyPrinter.printLineByLine(PrettyFormatter.getConnectingStatesString(self.currentNode), self.imagePrintSpeed)

    def isOver(self):
        return self.currentNode.hasNoConnectingStates()

    def getActionNumber(self, stateNode):
        highestValidActionNumber = len(stateNode.connectingStates) -1
        lowestValidActionNumber = 0

        actionNumber = -1
        inputIsValid = False
        while not inputIsValid:
            if (highestValidActionNumber == lowestValidActionNumber):
                PrettyPrinter.printCharacterByCharacter("Please press \"0\" then \"return\": ", \
                    100, self.textPrintSpeed)
            else:
                PrettyPrinter.printCharacterByCharacter("\nPlease enter an integer from %d to %d and then press \"return\": " % \
                    (lowestValidActionNumber, highestValidActionNumber), 100, self.textPrintSpeed)
            inputString = input("")
            try:
                actionNumber = int(inputString)
                if(actionNumber < lowestValidActionNumber or actionNumber > highestValidActionNumber):
                    raise(Exception("Input is an integer but is not in a valid range."))
                inputIsValid = True
            except:
                print("Sorry :-(, that was an invalid input.")
        
        return actionNumber
        