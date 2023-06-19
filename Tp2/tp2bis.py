running = True
studentData = {}

def addStudentData():
    studentName = input("Enter student name: ")
    studentData[studentName] = {"notes":{},"appreciation":""}

def addNote():
    studentName = input("Target Student: ")
    data = studentData[studentName]

    if data is None:
        print("The Student doesn't exist")
    else:
        noteName = input("Enter note name: ")
        noteValue = input("Enter note value: ")
        studentData[studentName]["notes"] = {noteName:noteValue}
def listData():
    print(studentData)

def setAppreciation():
    studentName = input("Target Student: ")
    data = studentData[studentName]
    if data is None:
        print("The Student doesn't exist")
    else:
        appreciation = input("Enter appreciation: ")
        studentData[studentName]["appreciation"] = appreciation

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
        running = False
    else:
        print("Command unknown")


while running:
    userInput = input("Enter command (ADD / NOTES /APPR / LIST /QUIT )")
    launchCommand(userInput)