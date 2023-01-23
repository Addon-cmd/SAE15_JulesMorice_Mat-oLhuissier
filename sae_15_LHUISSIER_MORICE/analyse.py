import csv
import stats
def csv_to_list(nomFichier):
    liste=[]
    with open(nomFichier+".csv", 'r') as fichier:
    # Création d'un lecteur CSV
        lecture = csv.reader(fichier)
    # Boucle sur chaque ligne du fichier
        
        for ligne in lecture:
            # Ajout de la ligne à la liste
            liste.append(ligne)

# Affichage de la liste pour vérifier que les données ont été récupérées
    return liste
#print(csv_to_list('velo'))

def moyenneCSV(nomFichier):
    liste_occupation=[]
    liste= csv_to_list(nomFichier)
    for i in range(0,len(liste)):
            liste_occupation.append(liste[i][3])
    return stats.moyenne(liste_occupation)
#print(moyenne_csv("voiture"))

def ecart_typeCSV(nomFichier):
    liste_occupation=[]
    liste= csv_to_list(nomFichier)
    for i in range(0,len(liste)):
            liste_occupation.append(liste[i][3])
    return stats.ecartType(liste_occupation)
#print(ecart_typeCSV("voiture"))

def varianceCSV(nomFichier):
    liste_occupation=[]
    liste= csv_to_list(nomFichier)
    for i in range(0,len(liste)):
            liste_occupation.append(liste[i][3])
    return stats.variance(liste_occupation)
#print(varianceCSV("voiture"))


def courbeCSV(nomFichier_voiture,nomFichier_velo):
    liste_occupation=[]
    liste_occupation2=[]
    liste_date=[]
    liste= csv_to_list(nomFichier_voiture)
    liste2= csv_to_list(nomFichier_velo)
    for i in range(1,len(liste)):
        date=liste[i][0]
        heure= date[3:5] + 'h' + date[6:8]        
        liste_date.append(heure)
        liste_occupation.append(round(float(liste[i][3]),2))
    for i in range(1,len(liste2)):     
        liste_occupation2.append(round(float(liste2[i][3]),2))
    return stats.courbe(liste_date,liste_occupation,liste_occupation2)
#print(courbeCSV("voiture","velo"))

