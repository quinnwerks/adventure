from statenode import StateNode
from stateformatter import StateFormatter
from prettyprinter import PrettyPrinter

class GameState:
    def __init__(self, startNode):
        self.__currentNode = startNode

    @property
    def currentNode(self):
        return self.__currentNode

    def changeStateDueToAction(self, actionNumber):
        connections = self.currentNode.connectingStates
        assert(actionNumber >= 0 and actionNumber < len(connections))
        self.__currentNode = connections[actionNumber]

    def printCurrentNode(self):
        textPrintSpeed = 0.05
        imagePrintSpeed = 0.1
        PrettyPrinter.printPrettyAsciiImage(self.currentNode.nodeImage, imagePrintSpeed)
        PrettyPrinter.printPrettyText(StateFormatter.formatText(self.currentNode), 100, textPrintSpeed)

    def isOver(self):
        return self.currentNode.hasNoConnectingStates()
        