# def factorielle_for(n)
a=int(input("entrez un nombre"))
resultat=1
for i in range(1,n+1):
        resultat*=i
        return resultat
    
  #def factorielle_while(n):
resultat= 1
i=1
while i<=n:
            resultat*=i
            i+=1
            return resultat
            print("factorielle de",n,"avec for:",factorielle_for(n))
            print("Factoriellede",n,"avec while:",factorielle_while(n))

    #afficher le nom et prenom selon les conditions de 1a50
            nom="idognon"
            prenom="Bienvenu"
            for i in range(1,50):
                if i%3==0 and i%5==0:
                    print(f"{i}:{nom},{prenom}")
                elif i%3==0:
                    print("f{i}:{nom}")
                elif i%5==0:
                    print(f"{i}:{pronom}")
          
