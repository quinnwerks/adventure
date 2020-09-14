from statenode import StateNode
from gamestate import GameState
from asciiimages import AsciiImages

def main():
    a = StateNode("You did action A!", AsciiImages.gameover())
    b = StateNode("You did action B!","")
    c = StateNode("blah", "")
    c.setConnectingStatesAndTheirActions([a,b], ["do a", "do b"])

    textPrintSpeed = 0.05
    imagePrintSpeed = 0.1
    game = GameState(c, textPrintSpeed, imagePrintSpeed)
    while(not game.isOver()):
        game.printCurrentNode()
        actionNumber = game.getActionNumber(game.currentNode)
        game.changeStateDueToAction(actionNumber)
    game.printCurrentNode()

if __name__ == '__main__':
    main()
