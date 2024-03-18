from services.connexion.DatabaseService import DatabaseService


def insertion_joueur(nom: str, prenom: str, sexe: str, categorie: {int, str}):
    db = DatabaseService()
    collection = db.get_collection("joueur")
    document = {
        "nom": nom,
        "prenom": prenom,
        "sexe": sexe,
        "categorie": {
            "age": categorie[0],
            "niveau": categorie[1]
        }
    }
    collection.insert_one(document)
    db.seDeconnecter()


