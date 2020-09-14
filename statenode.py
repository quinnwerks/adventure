class StateNode:  
    def __init__(self, nodeDescriptionText, nodeImage):
        self.__nodeDescriptionText = nodeDescriptionText
        self.__nodeImage = nodeImage
        self.__connectingStates = []
        self.__connectingStatesActions = []

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

    def setConnectingStatesAndTheirActions(self, connectingStates, connectingStatesActions):
        assert(len(connectingStates) == len(connectingStatesActions))
        self.__connectingStates = connectingStates
        self.__connectingStatesActions = connectingStatesActions

    def hasNoConnectingStates(self):
        return not self.connectingStates
