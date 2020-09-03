from statenode import StateNode
from gamestate import GameState
from stateformatter import StateFormatter
from prettyprinter import PrettyPrinter
from asciiimages import AsciiImages

def getActionNumber(stateNode):
    highestValidActionNumber = len(stateNode.connectingStates) -1
    lowestValidActionNumber = 0

    actionNumber = -1
    inputIsValid = False
    while not inputIsValid:
        PrettyPrinter.printPrettyText("\nPlease enter an integer from %d to %d: " % \
                (lowestValidActionNumber, highestValidActionNumber), 100, 0.05)
        inputString = input("")
        try:
            actionNumber = int(inputString)
            if(actionNumber < lowestValidActionNumber or actionNumber > highestValidActionNumber):
                raise(Exception("Input is an integer but is not in a valid range."))
            inputIsValid = True
        except:
            print("Sorry :-(, that was an invalid input.")
    
    return actionNumber


def main():
    a = StateNode("You did action A!", [], [], AsciiImages.heart())
    b = StateNode("You did action B!", [], [], "")
    c = StateNode("blah", [a, b], ["do a", "do b"], "")
    game = GameState(c)
    while(not game.isOver()):
        game.printCurrentNode()
        actionNumber = getActionNumber(game.currentNode)
        game.changeStateDueToAction(actionNumber)
    game.printCurrentNode()

if __name__ == '__main__':
    main()