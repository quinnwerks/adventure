class StateNode:
    def __init__(self, nodeDescriptionText, connectingStates, connectingStatesActions, nodeImage):
        assert(len(connectingStates) == len(connectingStatesActions))
        self.__nodeDescriptionText = nodeDescriptionText
        self.__connectingStates = connectingStates
        self.__connectingStatesActions = connectingStatesActions
        self.__nodeImage = nodeImage

    @property
    def nodeDescriptionText(self):
        return self.__nodeDescriptionText

    @property
    def connectingStates(self):
        return self.__connectingStates

    @property
    def connectingStatesActions(self):
        return self.__connectingStatesActions

    @property
    def nodeImage(self):
        return self.__nodeImage

    def hasNoConnectingStates(self):
        return not self.connectingStates
