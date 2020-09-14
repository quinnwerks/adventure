from statenode import StateNode

class PrettyFormatter:

    @staticmethod
    def getConnectingStatesString(stateNode):   
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
