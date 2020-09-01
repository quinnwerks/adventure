from statenode import StateNode
from stateformatter import StateFormatter
from prettyprinter import PrettyPrinter

class GameState:
    def __init__(self, startNode):
        self.__currentNode = startNode
        self.__textPrintSpeed = .05

    @property
    def currentNode(self):
        return self.__currentNode

    def changeStateDueToAction(self, actionNumber):
        connections = self.currentNode.connectingStates
        assert(actionNumber >= 0 and actionNumber < len(connections))
        self.__currentNode = connections[actionNumber]

    def printCurrentNode(self):
        PrettyPrinter.printPrettyText(StateFormatter.formatText(self.currentNode), 100, self.__textPrintSpeed)

    def isOver(self):
        return self.currentNode.hasNoConnectingStates()
        