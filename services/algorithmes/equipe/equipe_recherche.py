from services.connexion.DatabaseService import DatabaseService


def recherche_equipe_par_equipier(nom_joueur: str):
    db = DatabaseService()
    collections = db.get_collection("equipe")
    filtre = {
        "$or": [
            {"j1": nom_joueur},
            {"j2": nom_joueur}
        ]
    }
    projection = {"_id": 0}
    result = list(collections.find(filtre, projection))
    db.seDeconnecter()


def recherche_equipe_par_nombre(nom_equipe: str):
    db = DatabaseService()
    collections = db.get_collection("equipe")
    filtre = {
        {"nom": nom_equipe}
    }
    projection = {"_id": 0}
    result = list(collections.find(filtre, projection))
    db.seDeconnecter()

