class rentVelo:
    indirim=0.3
    
    def __init__(self,nom,nbr,prix):
        self.nom=nom
        self.nbr=nbr
        self.prix=prix
    
    print()
    print(f"{int(indirim *100)}% DE REDUCTION est OFFERTE APPARTIR DE 3 VELOS")
    print()
      
    def displaybike(self):  
      
        print(f"=>Velo_{self.nom} Disponible dans le stock ")
    
    @staticmethod
    def commendes(q,nbr):
        liste=[]
        count=0
        while q<=nbr:
            choix=input(f"entrer les velos_")
            count+=1
            if choix=="":
                return

            else:
                if count<=q:
                    liste.append(choix)
                    print(",".join(liste))
                else:
                        return
        else:
            print(f"nous disposons que {nbr} de velos au stoque ")

    def rentofbikes(self,q):
        phrase="Votre Facture total avec reduction "
        phras="Votre Facture total sans reduction "
        if q<=0:
            print(f"Entrer bien un nombre pour les velos ")
        if q>=3:
            rentVelo.commendes(q,self.nbr)
            total=self.prix+int(rentVelo.indirim)+q
            print()
            print(f"{phrase} est de {total}$")
        else:
            rentVelo.commendes(q,self.nbr)
            totale=self.prix*q
            print()
            print(f"{phras} est de {totale}$")
        