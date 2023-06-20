import os
import random
import numpy as np
import pandas as pd


	# on déclare le dictionnaire des élèves
dicEleves = { 
	'titi' : {'notes':{'tp1':10, 'tp2':13,'tp3':17}, 'appréciation': 'moyenne' }, 
	'toto' : {'notes' :{'tp1':19, 'tp2':11,'tp3':14}, 'appréciation': 'Très Bien' }, 
	'tata' : {'notes':{'tp1':15,'tp2':8,'tp3':13}, 'appréciation': 'Bonne' },
	'tutu' : {'notes':{'tp1':15,'tp2':13, 'tp3':12}, 'appréciation': 'Bonne' },
}

# on ajoute des élèves
for i in range(5,10) :	
	dicEleves['eleve'+str(i)] = {'notes':{'tp1':random.randint(0,20),'tp2':random.randint(0,20),'tp3':random.randint(0,20)}, 'appréciation': 'Bonne' }

# ajoute des notes aléatoire aux élèves
# on boucle sur les élèves
for eleve in dicEleves :
	# on boucle sur les notes de chaque élève
	for i in range(4,12) :
		# on ajoute une note aléatoire
		dicEleves[eleve]['notes']['tp'+str(i)] = random.randint(0,20)
		


# Création du DataFrame
df = pd.DataFrame.from_dict(dicEleves, orient='index')
print (df)

# Sélection des colonnes des notes des TP
df_notes = df['notes'].apply(pd.Series)
print (df_notes)
df_final = df_notes

# columnsList = []
# for i in range(1, 12) :
# 	columnsList.append('tp'+str(i))
# # Renommer les colonnes
# df_notes.columns = columnsList

# # Concaténer le DataFrame initial et les notes des TP
# df_final = pd.concat([df, df_notes], axis=1)
# df_final.drop('appréciation', axis=1, inplace=True)
# df_final.drop('notes', axis=1, inplace=True)
# Afficher le DataFrame final
print(df_final)

df_4col = df_final.iloc[:, 0:4]
print(df_4col)

filtreBool=np.array([True,False,True,False,True,False,True,False,True], dtype=bool)
df_impairs  = df_final.iloc[filtreBool, :]
print(df_impairs)
# alternative modulo
df_impairs  = df_final.iloc[::3, :]
print(df_impairs)


print("supérieur à 13 ----")
print(df_final > 13)
print("moyenne ----")
print (df_final.mean(numeric_only=True, axis=0))
print (df_final.mean(numeric_only=True, axis=1))
print("min ----")
print (df_final.min(numeric_only=True, axis=0))
print (df_final.min(numeric_only=True, axis=1))
print("max ----")
print (df_final.max(numeric_only=True, axis=0))
print (df_final.max(numeric_only=True, axis=1))