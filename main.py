class Entry:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description

entryList = []

def newEntry():
    print("Please enter the name of the entry")
    pEntry = Entry(input(), 0)
    print("Please enter the description of the entry")
    pEntry.description = input()
    entryList.append(pEntry)
    print("Entry has been created")
    newCommands()

def completeEntry():
    if not entryList:
        print("No entries entered yet")
        newCommands()
        return
    print("Please enter the name of the completed entry")
    name = input()
    for item in entryList:
        if name == item.getName():
            entryList.remove(item)
    print("Entry has been completed")
    newCommands()

def printEntryList():
    for item in entryList:
        print(str(item.getName()) + " Description: " + str(item.getDescription()) + "\n")
        newCommands()
    print("Entry List is empty")
    newCommands()

def start():
    print("Welcome! What would you like to do? \n \nPossible Tasks: newEntry, completeEntry, printEntryList")
    cmd = input()
    if cmd == "newEntry":
        newEntry()
    elif cmd == "completeEntry":
        completeEntry()
    elif cmd == "printEntryList":
        printEntryList()

def newCommands():
    print("Please enter the Next command. (List of Commands: newEntry, completeEntry, printEntryList)")
    cmd = input()
    if cmd == "newEntry":
        newEntry()
    elif cmd == "completeEntry":
        completeEntry()
    elif cmd == "printEntryList":
        printEntryList()


start()

# Rekursive Steuerungsaufrufe: Du rufst am Ende vieler Funktionen newCommands() bzw. newCommands() ruft wiederum die Funktionen auf. Dadurch entsteht mit der Zeit tiefe Rekursion — bei sehr vielen Aktionen kann das zu RecursionError führen. Sauberer wäre eine while-Schleife (eventuell später). Für jetzt: die minimalen Änderungen oben reichen, aber behalte das im Hinterkopf.

# Vergleich toleranter machen: Für Benutzerfreundlichkeit name = input().strip() und Vergleiche z.B. if name.strip().lower() == item.getName().strip().lower(): für case-insensitive Vergleich.

# printEntryList() ist OK: Die Funktion selbst ist in Ordnung — sie wird wahrscheinlich nicht ausgeführt wegen dem mehrfachen input()-Bug in start()/newCommands() oder weil keine Einträge existieren. Nach den obigen Fixes sollte sie wie erwartet funktionieren.

# Pythonic style: getName() / getDescription() sind in Ordnung, aber du könntest später Properties oder __str__ für Entry hinzufügen, um das Drucken zu vereinfachen.