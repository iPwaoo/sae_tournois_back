import datetime

from services.connexion.DatabaseService import DatabaseService


def insertion_tournoi(nom: str, nb_table: int, duree_max: int, date: datetime, lieu_nom: str, lieu_capacite: int, lieu_adresse_nom: str, lieu_adresse_rue: str, lieu_adresse_code_postal: str, objectif: str, format_tournoi: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    document = {
        "nom": nom,
        "nbTable": nb_table,
        "dureeMax": duree_max,
        "date": date,
        "lieu": {
            "nom": lieu_nom,
            "capacite": lieu_capacite,
            "adresse": {
                "nom": lieu_adresse_nom,
                "rue": lieu_adresse_rue,
                "codePostale": lieu_adresse_code_postal
            }
        },
        "objectif": objectif,
        "format": format_tournoi,
        "Matchs": []
    }
    collection.insert_one(document)
    db.seDeconnecter()


def insertion_match(id_joueur1: str, id_joueur2: str, heure: str, categorie: str):
    db = DatabaseService()
    collection = db.get_collection("match")
    document = {
        "joueurs": {
            "j1": id_joueur1,
            "j2": id_joueur2
        },
        "heure": heure,
        "categorie": categorie
    }
    collection.insert_one(document)
    db.seDeconnecter()

