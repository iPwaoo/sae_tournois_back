import connexion.DatabaseService as DB


def creer_un_joueur(nom: str, prenom: str, sexe: str, age: int, niveau: str):
    document = {}
    resultat = DB.DatabaseService.get_collection("joueurs").insert_one(document)
