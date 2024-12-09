import matplotlib.pyplot as plt
import numpy as np
def dessiner_cercle():
    try:
        rayon=float(input("Entrez le rayon du cercle:"))
        if rayon<=0:
            print("le rayon doit etre un nombre positif")
        return
    #generer les donnees pour le cercle
        theta=np.inspace(0.2*np.pi,100)
        x=rayon*np.cos(theta)
        y=rayon*np.sin(theta)
    #creer la figure et les axes plt.figure(figsize=(6.6))
        plt.plot(x,y,label=f"cercle de rayon{rayon}")
    #Ajuster les axes
        plt.gca().set_aspect('equal',abjustable='box')
        plt.axhline(0,color='black',linewidth=0.5)
        plt.grid(colo='gray',linestyle='--',linewidth=0.5)
    #Ajouter une iegende
        plt.legend()
    #Titre et affichage
        plt.title("Representation du cercle")
        plt.show()
        exceptValueError
        print("veuillez entrer un nombre valide pour le rayon.")
        #Appel de la fonction
            dessiner_cercle()
