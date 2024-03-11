def afficher_menu():
    while True:
        print("Bienvenue dans l'application de gestion des tournois de tennis de table")
        print("1. Inscrire un joueur")
        print("2. Organiser un tournoi")
        print("3. Afficher les résultats")
        print("4. Quitter")
        try:
            choix = input("Veuillez entrer le numéro de votre choix : ")
            choix = int(choix)
            if choix < 1 or choix > 4:
                raise ValueError
            return str(choix)
        except ValueError:
            print("Choix invalide. Veuillez entrer un numéro valide.")


def test():
    while True:
        choix = afficher_menu()

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