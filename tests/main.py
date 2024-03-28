from services.affichage import main_menu
import services.algorithmes.joueur.joueur_insertion as insertion
import services.algorithmes.joueur.joueur_recherche as recherche
import services.algorithmes.nombre_participants.mele_general_nombre_participants as mg


class Joueur:
    def __init__(self, nom, categorie, age, niveau):
        self.nom = nom
        self.categorie = categorie
        self.age = age
        self.niveau = niveau


def matchmaking(joueurs):
    # Séparer les joueurs en fonction de leur catégorie
    debutants = [joueur for joueur in joueurs if joueur.categorie == 'debutant']
    intermediaires = [joueur for joueur in joueurs if joueur.categorie == 'intermediaire']
    experts = [joueur for joueur in joueurs if joueur.categorie == 'expert']

    couples = []

    # Matcher les joueurs débutants
    couples.extend(matcher_joueurs(debutants))

    # Matcher les joueurs intermédiaires
    couples.extend(matcher_joueurs(intermediaires))

    # Matcher les joueurs experts
    couples.extend(matcher_joueurs(experts))

    return couples


def matcher_joueurs(joueurs):
    couples = []

    # Trier les joueurs par âge
    joueurs.sort(key=lambda x: x.age)

    # Diviser les joueurs en deux groupes égaux (ou aussi égaux que possible)
    groupe1 = joueurs[:len(joueurs) // 2]
    groupe2 = joueurs[len(joueurs) // 2:]

    # Créer des paires de joueurs équilibrées en termes d'âge et de niveau
    for joueur1 in groupe1:
        for joueur2 in groupe2:
            # Vérifier si la différence d'âge est acceptable et les niveaux sont proches
            if abs(joueur1.age - joueur2.age) <= 5 and joueur1.niveau == joueur2.niveau:
                couples.append((joueur1.nom, joueur2.nom))
                # Supprimer les joueurs appariés pour éviter les appariements multiples
                groupe2.remove(joueur2)
                break  # Passer au joueur suivant dans le premier groupe

    return couples


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
    # test()
    # result = insertion.insertion_joueur("BADI", "AOFO", "Femme", [25, 'Experte'])
    # print(result)
    # result = recherche.recherche_joueur("Quentin")
    # print(result)

    # Exemple d'utilisation
    # nombre_de_parties = int(input("Entrez le nombre de parties : "))
    # temps_disponible = input("Entrez le temps disponible (heures/minutes) : ")
    # nombre_max_participants = mg.calcul_max_participants(temps_disponible, nombre_de_parties)
    # print("Nombre maximum de participants possibles :", nombre_max_participants)

    # Exemple d'utilisation
    joueurs = [
        Joueur("Joueur1", "debutant", 20, "debutant"),
        Joueur("Joueur2", "debutant", 25, "intermediaire"),
        Joueur("Joueur3", "debutant", 30, "debutant"),
        Joueur("Joueur4", "intermediaire", 22, "debutant"),
        Joueur("Joueur5", "intermediaire", 28, "intermediaire"),
        Joueur("Joueur6", "intermediaire", 33, "expert"),
        Joueur("Joueur7", "expert", 26, "intermediaire"),
        Joueur("Joueur8", "expert", 31, "expert"),
        Joueur("Joueur9", "expert", 35, "expert")
    ]

    couples = matchmaking(joueurs)
    for couple in couples:
        print(couple)

# 65f850608f224eb1d47cd5f1
# 65f863b839df312113157054
