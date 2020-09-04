import time
import sys, termios

class PrettyPrinter:
    @staticmethod
    def printPrettyText(text, numColumns, printSpeed):
        currColumn = 0
        for char in text:
            if currColumn == numColumns:
                currColumn = 0
                print()

            print(char, end='')
            time.sleep(printSpeed)
            sys.stdout.flush() 
            currColumn = currColumn + 1
    
    @staticmethod
    def printPrettyAsciiImage(asciiImage, printSpeed):
        for char in asciiImage:
            if char == "\n":
                time.sleep(printSpeed)
            print(char, end='')
            sys.stdout.flush()