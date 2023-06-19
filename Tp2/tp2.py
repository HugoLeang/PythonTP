import os
import pathlib
import csv
import json

studentDatas = {'student1': {'notes': {'tp1': 10, 'tp2': 13, 'tp3': 17}, 'appreciation': 'moyenne'},
                'student2': {'notes': {'tp1': 19, 'tp2': 11, 'tp3': 14}, 'appreciation': 'très bien'},
                'student3': {'notes': {'tp1': 15, 'tp2': 8, 'tp3': 13}, 'appreciation': 'bonne'}}

studentsNoteResults = []

# Get current script running folder
parentFolder = pathlib.Path(__file__).parent.resolve()
print(parentFolder)

# Create general "students" directory
studentsDir = os.path.join(parentFolder, "students")
if not os.path.exists(studentsDir):
    os.mkdir(studentsDir)
    os.chdir(studentsDir)

for data in studentDatas:
    # Create student specific directory and change directory
    os.mkdir(data)
    os.chdir(data)
    # Create appreciation file .txt
    appreciationFile = open('appreciation.txt', 'w')
    appreciationFile.write(studentDatas[data].get('appreciation'))
    appreciationFile.close()
    # Create CSV file
    notes = studentDatas[data].get('notes')
    field = []
    noteDatas = []
    with open('notes.csv', 'w', newline='') as noteFile:
        writer = csv.writer(noteFile)

        for note in notes:
            field.append(note)
            noteDatas.append(notes.get(note))

        writer.writerow(field)
        writer.writerow(noteDatas)

    moyenne = sum(noteDatas) / len(noteDatas)
    maxNote = max(noteDatas)
    minNote = min(noteDatas)
    studentsNoteResults.append({data: {'moyennes': moyenne, 'max': maxNote, 'min': minNote}})
    os.chdir("..")

jsonObject = json.dumps(studentsNoteResults, indent=4)
with open("studentNoteResults.json", "w") as outfile:
    outfile.write(jsonObject)

