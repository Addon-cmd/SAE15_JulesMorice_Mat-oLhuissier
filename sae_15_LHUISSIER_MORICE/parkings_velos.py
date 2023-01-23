import requests
from lxml import etree 
import time
from datetime import datetime
import json

#Noms des parkings de montpellier
parkings=['FR_MTP_ANTI','FR_MTP_COME','FR_MTP_CORU','FR_MTP_EURO','FR_MTP_FOCH','FR_MTP_GAMB','FR_MTP_GARE','FR_MTP_TRIA','FR_MTP_ARCT',
'FR_MTP_PITO','FR_MTP_CIRC','FR_MTP_SABI','FR_MTP_GARC','FR_MTP_MOSS','FR_STJ_SJLC','FR_MTP_MEDC','FR_MTP_OCCI','FR_CAS_VICA','FR_MTP_GA109','FR_MTP_GA250','FR_CAS_CDGA','FR_MTP_ARCE','FR_MTP_POLY'] 


#fonction qui permet de suivre l'occupation d'un parking en particulier (un dans le tableau ci-dessus) et qui enregistre le résultat dans un fichier txt
def parking(nomParking,nomFichier):
    
    date=time.time()
    response=requests.get("https://data.montpellier3m.fr/sites/default/files/ressources/"+nomParking+'.xml')
    f1=open(nomParking+".txt","w", encoding='utf8') #Creation d'un fichier txt s'il n'existe pas, sinon l'ecrase et l'ouvre en mode ecriture 
    f1.write(response.text) #ecriture de la requete dans le fichier txt 
    f1.close() #fermeture du fichier 

    tree = etree.parse(nomParking+".txt")

    for user in tree.xpath("Status"):
        if user.text=='Open':
            date = time.strftime('%d-%H_%M_%S', time.localtime(date))
            for user in tree.xpath('Free'):
                free=int(user.text)
            for user in tree.xpath('Total'):
                occupation=100-round((free/int(user.text))*100,2)
                f1=open(nomFichier+'.csv','a', encoding='utf8')
                f1.write(f"{date},{str(free)},{str(user.text)},{str(occupation)} \n")
                
                f1.close()

    
def velo(nomFichier):

    ParkVelo=requests.get(f"https://montpellier-fr-smoove.klervi.net/gbfs/en/station_status.json")
    f1=open(f"ParkVelo.json","w", encoding='utf8') # J'ouvre mon fichier txt de chaque parkings en ecriture format utf8
    f1.write(ParkVelo.text) # j'ecrit dans mon dossier les infos que je recupere du site 
    f1.close() # je ferme mon fichier

    fileObject = open("ParkVelo.json", "r")
    jsonContent = fileObject.read()
    aList = json.loads(jsonContent)
    free=(aList['data']['stations'][10]['num_bikes_available'])
    total=(aList['data']['stations'][10]['num_docks_available'])
    date=(aList['data']['stations'][10]['last_reported'])
    date = time.strftime('%d-%H_%M_%S', time.localtime(date))

    occupation=100-round((free/(total+free))*100,2)
    f1=open(nomFichier+'.csv','a', encoding='utf8')
    f1.write(f"{date},{str(free)},{str(int(total+free))},{str(occupation)} \n")
    f1.close()
    fileObject.close()
