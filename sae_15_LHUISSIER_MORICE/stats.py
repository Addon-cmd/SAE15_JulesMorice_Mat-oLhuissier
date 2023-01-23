#module de calculs de stats
#copyright Mateo Lhuissier & Jules Morice
#version 1.1
#20/01/2023

#Importations des modules
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

#Fonctions
#Calcul de la moyenne d'une liste de nombres
def moyenne(liste_nbr):
    moyenne=0
    for i in liste_nbr:
        moyenne+=float(i)
    moyenne/=len(liste_nbr)
    return round(moyenne,2)

#Calcul de la variance d'une liste de nombres
def variance(liste_nbr):
    variance=0
    for i in liste_nbr:
        variance+=(float(i)-moyenne(liste_nbr))**2
    variance/=len(liste_nbr)
    return round(variance,2)

#Calcul de l'ecart type d'une liste de nombres
def ecartType(liste_nbr):
    ecart_type=0
    for i in liste_nbr:
        ecart_type+=(float(i)-moyenne(liste_nbr))**2
    ecart_type/=len(liste_nbr)
    ecart_type=sqrt(ecart_type)
    return round(ecart_type,2)

#Calcul de la covariance d'une liste de nombres
def covariance(liste1,liste2):
    covariance=0
    for i in range(len(liste1)):
        covariance+=(liste1[i]-moyenne(liste1)*(liste2[i]-moyenne(liste2)))
        covariance/=len(liste1)
        return covariance

#Calcul de la coorelation d'une liste de nombres
def coorelation(liste1,liste2):
    coorelation=0
    for i in range(len(liste1)):
        coorelation+=(liste1[i]-moyenne(liste1)*(liste2[i]-moyenne(liste2)))
        coorelation/=len(liste1)
        coorelation/=ecartType(liste1)*ecartType(liste2)
        return coorelation

#Affiche une courbe avec l'axe des X en premier, puis l'axe des Y, puis en option une 2eme courbe 
def courbe(axe_x,axe_y,axe_y2=0):
    plt.ylim([0, 110])
    
    plt.plot(axe_x,axe_y,marker="o",label="voiture")
    plt.plot(axe_x,axe_y2,label="vélo",marker="o")
    plt.legend()

    for x,y in zip(axe_x,axe_y):

        label = "{:.2f}".format(y)

        plt.annotate(label, 
                    (x,y), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center') 
    for x,y in zip(axe_x,axe_y2):

        label = "{:.2f}".format(y)

        plt.annotate(label,
                    (x,y), 
                    textcoords="offset points",
                    xytext=(0,10), 
                    ha='center') 
    plt.show()
