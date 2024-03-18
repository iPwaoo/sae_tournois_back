from services.connexion.DatabaseService import DatabaseService


def recherche_joueur(objet_de_recherche: str):
    db = DatabaseService()
    collections = db.get_collection("joueur")
    filtre = {
        "$or": [
            {"nom": objet_de_recherche},
            {"prenom": objet_de_recherche}
        ]
    }
    projection = {"nom": 1, "prenom": 1, "_id": 0}
    result = collections.find(filtre, projection)
    for document in result:
        print(document)
    db.seDeconnecter()
