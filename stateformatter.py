from statenode import StateNode

class StateFormatter:

    @staticmethod
    def __getConnectingStatesString(stateNode):   
        connectingStatesString = ""     
        if stateNode.hasNoConnectingStates():
            connectingStatesString = ""
        else:
            connectingStatesString = "Actions:\n"

        i = 0
        actions = stateNode.connectingStatesActions
        for stateNodeAction in actions:
            connectingStatesString += str(i) + ": " + stateNodeAction + "\n"
            i = i + 1

        return connectingStatesString

    @staticmethod
    def format(stateNode):
        connectedStatesString = StateFormatter.__getConnectingStatesString(stateNode)
        return stateNode.nodeDescriptionText + "\n" + connectedStatesString