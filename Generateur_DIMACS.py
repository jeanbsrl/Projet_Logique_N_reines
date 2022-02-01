# Programme en Python qui crée un fichier DIMACS représentant l'instance des N-Reines avec le N pré-saisi.

import sys

# Fonction pour une formule logique sous forme normale conjonctive
# lorsqu'au moins une variable de la clause Z doit être vraie
def au_moins_une_reine(Z):
    clauses = ""
    for x in Z:
        clauses = clauses + " " + str(x)
    clauses = clauses + " 0\n"
    return clauses

# Fonction pour une formule logique sous forme normale conjonctive
# lorsqu'au plus une variable de la clause Z doit être vraie
def au_plus_une_reine(Z):
    clauses = ""
    for x in Z:
        for y in Z[Z.index(x) + 1:]:
            clauses = clauses + " -" + str(x) + " -" + str(y) + " 0\n"
    return clauses

# Fonction pour une formule logique sous forme normale conjonctive
# lorsqu'une et une seule seule (exactement une) variable de la clause Z doit être vraie
def une_seule_reine(Z):
    clauses = ""
    clauses = clauses + au_moins_une_reine(Z)
    clauses = clauses + au_plus_une_reine(Z)
    return clauses

# Fonction de la position dans la grille (en considérant que les cases sont numérotées de 1 à N * N)
def pos_variable(r, c, n):
    return r * n + c + 1

# Lecture de N
if len(sys.argv) > 1:
    N = int(sys.argv[1])
else:
    N = 3
if N < 1:
    print("Erreurr N<1")
    sys.exit(0)

# Création (Ouverture) du fichier DIMACS
f = open("%d_reines.cnf" % N, "w+")

# Commentaires du début de fichier
f.write("c Expression du problème des N-Reines en SAT pour N=" + str(N) + "\n")
cases = N * N
f.write("c L'échiquier possède " + str(cases) + " positions\n")

# Clauses d'une et une seule reine par ligne
clauses = ""
for ligne in range(0, N):
    A = []
    for colonne in range(0, N):
        position = pos_variable(ligne, colonne, N)
        A.append(position)
    clauses = clauses + une_seule_reine(A)

# Clauses d'une et une seule reine par colonne
for colonne in range(0, N):
    A = []
    for ligne in range(0, N):
        position = pos_variable(ligne, colonne, N)
        A.append(position)
    clauses = clauses + une_seule_reine(A)

# Clauses d'au plus une reine par diagonale
for ligne in range(N-1, -1, -1):
    A = []
    for x in range(0, N-ligne):
        position = pos_variable(ligne+x, x, N)
        A.append(position)
    clauses = clauses + au_plus_une_reine(A)

for colonne in range(1, N):
    A = []
    for x in range(0, N-colonne):
        position = pos_variable(x, colonne+x, N)
        A.append(position)
    clauses = clauses + au_plus_une_reine(A)

for ligne in range(N-1, -1, -1):
    A = []
    for x in range(0, N-ligne):
        position = pos_variable(ligne+x, N-1-x, N)
        A.append(position)
    clauses = clauses + au_plus_une_reine(A)

for colonne in range(N-2,  -1,  -1):
    A = []
    for x in range(0, colonne + 1):
        position = pos_variable(x, colonne-x, N)
        A.append(position)
    clauses = clauses + au_plus_une_reine(A)

nbrclauses = clauses.count('\n')

# Ecriture de la ligne qui spécifie qu'il s'agit d'une forme normale conjonctive, avec le nombre de variables
# et le nombre de clauses disjonctives que le fichier DIMACS contient
f.write('p cnf ' + str(N * N) + ' ' + str(nbrclauses) + '\n')
f.write(clauses)

f.close()
