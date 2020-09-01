from statenode import StateNode
from gamestate import GameState
from stateformatter import StateFormatter

def getActionNumber(stateNode):
    highestValidActionNumber = len(stateNode.connectingStates) -1
    lowestValidActionNumber = 0

    actionNumber = -1
    inputIsValid = False
    while not inputIsValid:
        inputString = input("Please enter an action: ")
        try:
            actionNumber = int(inputString)
            if(actionNumber < lowestValidActionNumber or actionNumber > highestValidActionNumber):
                raise(Exception("Input is an integer but is not in a valid range."))
            inputIsValid = True
        except:
            print("Sorry :-(, that was an invalid input.\nPlease enter an integer from %d to %d\n" % \
                (lowestValidActionNumber, highestValidActionNumber))
    
    return actionNumber


def main():
    a = StateNode("You did nothing!", [], [])
    b = StateNode("You did poopie!", [], [])
    c = StateNode("blah", [a, b], ["do nothing", "poopself"])
    game = GameState(c)
    while(not game.isOver()):
        game.printCurrentNode()
        actionNumber = getActionNumber(game.currentNode)
        game.changeStateDueToAction(actionNumber)
    game.printCurrentNode()

if __name__ == '__main__':
    main()