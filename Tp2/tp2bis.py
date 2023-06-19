import json
import os

# --------------------------
# ------- FUNCTION ---------
# --------------------------

# Function Add a student
def addStudentData():
    studentName = input("Enter student name: ")
    studentData[studentName] = {"notes": {}, "appreciation": ""}

# Function Change note of student
def addNote():
    studentName = input("Target Student: ")
    data = studentData[studentName]

    if data is None:
        print("The Student doesn't exist")
    else:
        noteName = input("Enter note name: ")
        noteValue = input("Enter note value: ")
        studentData[studentName]["notes"] = {noteName: noteValue}

# Function list noe and apreciation
def listData():
    print(studentData)

# Function change appreciation
def setAppreciation():
    studentName = input("Target Student: ")
    data = studentData[studentName]
    if data is None:
        print("The Student doesn't exist")
    else:
        appreciation = input("Enter appreciation: ")
        studentData[studentName]["appreciation"] = appreciation

def saveAllData():
    jsonObject = json.dumps(studentData, indent=4)
    with open("save.json", "w") as outfile:
        outfile.write(jsonObject)

def loadAllData():
    global studentData
    if os.path.exists("save.json"):
        with open("save.json", "r") as f:
            studentData = json.load(f)

# ----------------------------------------------

running = True
studentData = {}
loadAllData()

# ----------------------------------------------

def launchCommand(commandInput):
    global running
    processedCommand = commandInput.lower()
    if processedCommand == "add":
        addStudentData()
    elif processedCommand == "appr":
        setAppreciation()
    elif processedCommand == "notes":
        addNote()
    elif processedCommand == "list":
        listData()
    elif processedCommand == "quit":
        saveAllData()
        running = False
    else:
        print("Command unknown")


while running:
    userInput = input("Enter command (ADD / NOTES /APPR / LIST /QUIT )")
    launchCommand(userInput)