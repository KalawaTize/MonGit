# data_manipulation.py
import pandas as pd
import numpy as np


# ===== Exercice 1 =====
# 1. Création et sauvegarde du fichier etudiants.csv
# df_etudiants = pd.DataFrame({
#                             'Nom': ['Alice', 'Bob', 'Claire', 'David', 'Emma'],
#                             'Age': [21, 22, 20, 23, 22],
#                             'Moyenne': [17.5, 13.2, 15.6, 9.5, 14.8],
#                             'Filière': ['Info', 'Maths', 'Physique', 'Chimie', 'Info']
# })



#df_etudiants.to_csv("etudiants.csv", index=False)
# 2. Chargement
df_students = pd.read_csv("etudiants.csv")

# 3. Affiche les 5 premières lignes
#print(df_students.head())
#print(df_students[df_students["Age"]>22])
#print(df_students.info())
print(df_students.describe())

#print(df_students[df_students["Moyenne"]>15])


