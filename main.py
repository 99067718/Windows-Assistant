import os
import webScrape as webSc
from time import sleep as wait
def splitForCommand(input):
    import re
    split_command = re.findall(r'(?:[^\s,"\']|"(?:\\.|[^"])*"|\'(?:\\.|[^\'])*\')+', input)
    return split_command

def stripQuotesFromArray(split_command):
    split_command = [word.strip("'\"") for word in split_command]
    return split_command
# print(title)
def Request(question = "Your request: ", type = "input"):
    if type == "input":
        answer = input(question)
        return answer
    elif type == "exec":
        codeToRun = input(question)
        try:
            exec(codeToRun)
        except Exception as ex:
            print(ex)
    else:
        print("The selected 'Type' doesn't exist")
        
    Request()

def clearConsole():
    os.system('cls')

def rickRoll():
    clearConsole()
    print("""
     o
    ||\\
    / \\
    """)
    wait(0.2)
    clearConsole()
    print("""
     o
    /||
    / \\
    """)
    wait(0.2)
    clearConsole()
    print("""
     o
    ||\\
    / \\
    """)
    wait(0.2)
    clearConsole()
    print("""
     o
    /|\\
    | |
    """)
    wait(0.2)
    clearConsole()
    print("""
    _o_
   / | \\
    / \\
    """)

while True:
    try:
        answer = Request()
        if answer == "help":
            print("Here's the list of commands \n1. execute\n2. print\n3. clear")
        elif answer == "execute":
            Request(question="Enter your code here: ", type="exec")
        elif answer == "print":
            print(Request("String to print: "))
        elif answer == "clear":
            print("Clearing Console...")
            wait(1)
            clearConsole()
            print("Console succesfully cleared!")
        elif answer == "rickroll":
            rickRoll()
        else:
            webSc.inputQuestion(answer)
    except Exception as ex:
        print("Something went wrong:")
        print(ex)