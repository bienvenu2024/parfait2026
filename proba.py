def compter_facons_somme(somme_cible,des_restant,face):
    if des_restant==0:
        return 1
    if somme_cible==0 :
        else0
        if somme_cible<0:
            return 0
        facons=0
        for face in range(1,face+1):
            facons+=compter_facons_somme(somme_cible-face,des_restant-1,faces)
            return facons
        #parametre
        somme_cible=20
        nombre_de_des=5
        nombre_de_faces=6
        #calcul
        nombre_de_facons=compter_facons_somme(somme_cible,nombre_de_des,nombre_de_face)
        #Afficher du resultat
        print(f"le nombre de façons differentes d'obtenir"
              {somme_cible} avec {nombre_de_des}dés à {nombre_de_face}face est:{nombre_de_facons} )
    
        
    
    
    
