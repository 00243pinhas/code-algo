

from codes1 import *
from code2 import*


def affiche(affich):
     print(f"entrez")
     ch=input(f"Yes or No _")
     print()
     if ch=="Yes":
          for x in affich:
               print(f"categorie_{x}")
     else:
          affiche(affich)

def categorie_choix(Categorie):
     affiche(Categorie)
     while True:
          print()
          print(f"NB...clique enter if u finish your commande ")
          choix=input("entrer un les categorie_")
          if choix=="":
               return
          else:
               if choix==Categorie[0]:
                    while True:
                         U_input=int(input("""
                         1 Display Velos available
                         2 Rent bikes 
                         3 Exit 
                              """))
                         
                         if U_input==1:
                              for x in velohotaire:
                                   x.displaybike()
                         elif U_input==2:
                              q=int(input(f"entrer le nombre de velos que tu veux_"))
                              velo1.rentofbikes(q)
                         else:
                              break

               elif choix==Categorie[1]:
                    while True:
                         U_input=int(input("""
                         1 Display Velos Available 
                         2 Rent a/bikes
                         3 Exit
                         """))

                         if U_input==1:
                              for x in veldocotidien:
                                   x.displaybike()
                         elif U_input==2:
                              q=input(f"entrer Votre nbr velos_")
                              try:
                                   n=int(q)
                                   veloa.rentofbikes(n)
                              except:
                                   print(f"Erreur...Bien lire ")
                         else:
                              break
                
               elif choix==Categorie[2]:
                    while True:
                         U_input=int(input("""
                         1 Display Velos Available 
                         2 Rent a/bikes
                         3 Exit
                         """))

                         if U_input==1:
                              for x in velohebdomadaire:
                                   x.displaybike()
                         elif U_input==2:
                              q=input(f"entrer Votre nbr velos_")
                              try:
                                   n=int(q)
                                   veloP.rentofbikes(n)
                              except:
                                   print(f"Erreur...Bien lire ")
                         else:
                              break

categorie_choix(Categorie1)