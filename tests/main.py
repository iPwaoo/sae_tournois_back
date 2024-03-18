from services.affichage import main_menu
import services.algorithmes.joueur.joueur_insertion as insertion
import services.algorithmes.joueur.joueur_recherche as recherche


def test():
    while True:
        choix = main_menu.afficher_menu()
        if choix == "1":
            # Logique pour inscrire un joueur
            print("Vous avez choisi d'inscrire un joueur.")
        elif choix == "2":
            # Logique pour organiser un tournoi
            print("Vous avez choisi d'organiser un tournoi.")
        elif choix == "3":
            # Logique pour afficher les résultats
            print("Vous avez choisi d'afficher les résultats.")
        elif choix == "4":
            print("Merci d'avoir utilisé l'application. À bientôt !")
            break
        else:
            print("Choix invalide. Veuillez entrer un numéro valide.")


if __name__ == '__main__':
    #test()
    #result = insertion.insertion_joueur("BADI", "AOFO", "Femme", [25, 'Experte'])
    #print(result)
    result = recherche.recherche_joueur("Quentin")
    print(result)

#65f850608f224eb1d47cd5f1
#65f863b839df312113157054