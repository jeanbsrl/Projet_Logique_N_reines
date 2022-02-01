# Après avoir passé le contenu du fichier CNF auprès du SAT-solveur (sur le site ci-dessous)
# https://msoos.github.io/cryptominisat_web/#
# Copier le résultat du site dans le fichier .txt "traceSAT".
# Ce programme en Python affiche la solution du problème de manière compréhensible.

# Lecture de la premiere lettre de chaque ligne
# if c skip
# if s SATISFIABLE continuer vers v
# if s UNSATISFIABLE afficher "Insatisfaisable, pas de solution."
# if v representer

def parcours_trace(f):
    x = 'c'
    while x == 'c':
        for line in f:
            x = f.read(line(1))
    return x

def generer_echiquier():
    g = open("representation_echiquier", "w+")
        # pour i allant de 0 à N*N:
        #   pour j allant de 0 à N:
        #       si lecture_numero_de_la_case > 0:
        #           ecrire "R |"
        #       else: ecrire "  |"
        #   ecrire "-----------------------------------------------"
    g.write("echiquier")
    g.close()

f = open("traceSAT.txt", "r")

x = parcours_trace(f)
if x == 's':
    y = f.read(3)
    if y == 'U':
        print("Insatisfaisable, pas de solution.")
    elif y == 'S':
        v = parcours_trace(f)
        if v == 'v':
            generer_echiquier()
