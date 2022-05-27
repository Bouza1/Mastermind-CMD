import random
import os

global count
count = 10
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(numbers)
generatedArray = []
guessArray=[]
incorrectArray = []

def mainMenu():
    clearConsole()
    print("============== MENU ==============")
    print("Enter C to play against computer or H to play against a human")
    userinp = input()
    if userinp == "c" or userinp == "C":
        for i in range (4):
            compNumbers = numbers[0+i]
            generatedArray.append(compNumbers)
        playGame()
    elif userinp == "h" or userinp == "H":
        print("Enter the 1st Number Of The Key")
        number1 = int(input())
        print("Enter the 2nd Number Of The Key")
        number2 = int(input())
        print("Enter the 3rd Number Of The Key")
        number3 = int(input())
        print("Enter the 4th Number Of The Key")
        number4 = int(input())
        generatedArray.clear()
        generatedArray.append(number1)
        generatedArray.append(number2)
        generatedArray.append(number3)
        generatedArray.append(number4)
        print(generatedArray)
        clearConsole()
        playGame()

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def playGame():
    resultArray=[]

    def guess():
        global count
        if count == 0:
            clearConsole()
            print("========== End Of Game, Unlucky ==========")
        else:
            print("Enter Your Guesses Below:")
            print("Enter the 1st Number:")
            input1 = int(input())
            print("Enter the 2nd Number:")
            input2 = int(input())
            print("Enter the 3rd Number:")
            input3 = int(input())
            print("Enter the 4th Number:")
            input4 = int(input())
            guessArray.append(input1)
            guessArray.append(input2)
            guessArray.append(input3)
            guessArray.append(input4)
            #1st number of guess
            if guessArray[0] == generatedArray[0]:
                resultArray.append("Bull")
            elif guessArray[0] == generatedArray[1] or guessArray[0] == generatedArray[2] or guessArray[0] == generatedArray[3]:
                resultArray.append("Cow")
            elif guessArray[0] != generatedArray[0] or guessArray[0] != generatedArray[1] or guessArray[0] != generatedArray[2] or guessArray[0] != generatedArray[3]:
                resultArray.append("Incorrect")
                incorrectArray.append(guessArray[0])
            #2nd number of guess
            if guessArray[1] == generatedArray[1]:
                resultArray.append("Bull")
            elif guessArray[1] == generatedArray[0] or guessArray[1] == generatedArray[2] or guessArray[1] == generatedArray[3]:
                resultArray.append("Cow")
            elif guessArray[1] != generatedArray[1] or guessArray[1] != generatedArray[0] or guessArray[1] != generatedArray[2] or guessArray[1] != generatedArray[3]:
                resultArray.append("Incorrect")
                incorrectArray.append(guessArray[1])
            #3rd number of guess
            if guessArray[2] == generatedArray[2]:
                resultArray.append("Bull")
            elif guessArray[2] == generatedArray[0] or guessArray[2] == generatedArray[1] or guessArray[2] == generatedArray[3]:
                resultArray.append("Cow")
            elif guessArray[2] != generatedArray[0] or guessArray[2] != generatedArray[1] or guessArray[2] != generatedArray[2] or guessArray[2] != generatedArray[3]:
                resultArray.append("Incorrect")
                incorrectArray.append(guessArray[2])
            #4th number of guess
            if guessArray[3] == generatedArray[3]:
                resultArray.append("Bull")
            elif guessArray[3] == generatedArray[0] or guessArray[3] == generatedArray[1] or guessArray[3] == generatedArray[2]:
                resultArray.append("Cow")
            elif guessArray[3] != generatedArray[0] or guessArray[3] != generatedArray[1] or guessArray[3] != generatedArray[2] or guessArray[3] != generatedArray[3]:
                resultArray.append("Incorrect")
                incorrectArray.append(guessArray[3])
            print(resultArray)
            if resultArray[0] == "Bull" and resultArray[1] == "Bull" and resultArray[2] == "Bull" and resultArray[3] == "Bull":
                print("Congratulations You Win")
            else:   
                clearConsole()
                print(guessArray)
                print(resultArray)
                print("======== Try Again =======")
                count = count - 1
                print("You Have", count, "Goes Left")
                print("Incorrect Numbers Previously Guessed")
                print(incorrectArray)
                guessArray.pop(0)
                guessArray.pop(0)
                guessArray.pop(0)
                guessArray.pop(0)
                resultArray.pop(0)
                resultArray.pop(0)
                resultArray.pop(0)
                resultArray.pop(0)
                guess()
    guess()




mainMenu()