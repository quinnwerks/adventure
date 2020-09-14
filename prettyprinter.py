import time
import sys, termios

class PrettyPrinter:
    @staticmethod
    def printCharacterByCharacter(text, numColumns, printSpeed):
        for char in text:
            print(char, end='')
            time.sleep(printSpeed)
            sys.stdout.flush() 
    
    @staticmethod
    def printLineByLine(asciiImage, printSpeed):
        for char in asciiImage:
            if char == "\n":
                time.sleep(printSpeed)
            print(char, end='')
            sys.stdout.flush()