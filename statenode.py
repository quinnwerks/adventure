class StateNode:
    def __init__(self, nodeDescriptionText, connectingStates, connectingStatesActions):
        assert(len(connectingStates) == len(connectingStatesActions))
        self.__nodeDescriptionText = nodeDescriptionText
        self.__connectingStates = connectingStates
        self.__connectingStatesActions = connectingStatesActions

    @property
    def nodeDescriptionText(self):
        return self.__nodeDescriptionText

    @property
    def connectingStates(self):
        return self.__connectingStates

    @property
    def connectingStatesActions(self):
        return self.__connectingStatesActions

    def hasNoConnectingStates(self):
        return not self.connectingStates
