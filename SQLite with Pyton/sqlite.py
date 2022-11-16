# -*- coding: utf-8 -*-
"""SQLite.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DjNjUkCQMPM-97zfKUEwVTX9SwEFB0H2

La Fonction connect() retourne une instance de connexion qui maintient la connexion à la base de données. Cela permet d'écrire des requetes,... d'ajouter les données dans la base
"""

import sqlite3

# connect()
con = sqlite3.connect('jobs.db')

"""**Creer un curseur et executer une requete SQL en python**

Un curseur de la classe Cursor permet

*   d'executer une requete auprès de la base de données
*   d'analyser les résultats de la base de données
*   convertir les resultats en objets python
*   de stocker les résultats dans des variables locales
"""

# cursor()

cursor = con.cursor()

# afficher touttes les colonnes de la table
query = "select* from recent_grads"

# execute la requete situé dans la variable query et ce cursor convertie les resultats en tuple, stocke dansune
# variable locale
cursor.execute(query)

# Chercher tout les résultats qu'on n'a recuperer sous la forme d'une liste de tuples et qu'on assigne à la variable results
results = cursor.fetchall()

print(results[0:5])

"""

*   Requete SQL qui retourne toutes les valeurs de la colonne Major depuis la table recent_grads.
*   Stocker les résultats(list de tuples) et assigner les à la variable majors
*   afficher les 5 premiers tuples de résultats de majors

"""

query = "select Major from recent_grads"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[0:5])

"""# **Chercher un certain nombre de résultats**"""

# fetchone()
# fetchmany(n)
import sqlite3 as sq
con = sq.connect('jobs.db')
cursor = con.cursor()
query = "select Major from recent_grads"
cursor.execute(query)

first_result = cursor.fetchone()
second_result = cursor.fetchone()
print(first_result)
print(second_result)

next_five_results = cursor.fetchmany(5)
print(next_five_results)

"""# **Stopper la connexion à la base de données**"""

# close()
con = sq.connect('jobs.db')
con.close()

"""*  Connexion à la base de données jobs2.db
*  requete SQL qui retourne toutes les majors dans l'ordre alphabétique inverse
*  Assigner le resultat complet à la variable result
*  Fermer la connexion à la base de données
"""

import sqlite3 as sq
con = sq.connect('jobs2.db')
cursor = con.cursor()
query = "select Major from recent_grads order by Major DESC"
cursor.execute(query)
result = cursor.fetchall()
con.close()

print(result)