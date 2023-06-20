import numpy as np
marks = {"StudentA": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentB": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentC": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentD": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentE": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentF": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentH": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentI": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentJ": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }},
         "StudentK": {"marks": {"tp1": 15.3, "tp2": 12, "tp3": 16, "tp4": 9, "tp5": 10 }}}

studentData =[]
npArray = np.array([0,0,0,0,0,0])
for student in marks:
    data = []
    #data.append(student)
    markValues = list(marks[student]["marks"].values())
    for value in markValues:
        data.append(value)
    studentData.append(data)


npArray = np.array(studentData)


print(npArray)