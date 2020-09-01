from statenode import StateNode
from stateformatter import StateFormatter

class GameState:
    def __init__(self, startNode):
        self.__currentNode = startNode

    @property
    def currentNode(self):
        return self.__currentNode

    def changeStateDueToAction(self, actionNumber):
        connections = self.currentNode.connectingStates
        assert(actionNumber >= 0 and actionNumber < len(connections))
        self.currentNode = connections[actionNumber]

    def printCurrentNode(self):
        print(StateFormatter.format(self.currentNode))

    def isOver(self):
        return self.currentNode.hasNoConnectingStates()
        