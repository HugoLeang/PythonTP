import json
import os
import pathlib
import csv

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
    global studentData
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

def studentsNoteResult():
    global studentData
    studentsNoteResults = []

    for data in studentData:
        notes = studentData[data].get('notes')
        noteDatas = []
        for note in notes:
            noteDatas.append(int(notes.get(note)))

        moyenne = sum(noteDatas) / len(noteDatas)
        maxNote = max(noteDatas)
        minNote = min(noteDatas)
        studentsNoteResults.append({data: {'moyennes': moyenne, 'max': maxNote, 'min': minNote}})
        os.chdir("..")

    jsonObject = json.dumps(studentsNoteResults, indent=4)
    with open("studentNoteResults.json", "w") as outfile:
        outfile.write(jsonObject)

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
        studentsNoteResult()
        saveAllData()
        running = False
    else:
        print("Command unknown")


while running:
    userInput = input("Enter command (ADD / NOTES /APPR / LIST /QUIT )")
    launchCommand(userInput)