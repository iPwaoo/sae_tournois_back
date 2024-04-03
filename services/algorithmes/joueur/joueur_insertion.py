from services.connexion.DatabaseService import DatabaseService


def insertion_joueur(genre: str, nom: str, prenom: str, age: int, courriel: str, telephone: str, adresse: str, codePostale: int, ville: str, pays: str, numeroInscription: str, licence: str, classement: int):
    db = DatabaseService()
    collection = db.get_collection("joueur")
    document = {
        "genre": genre,
        "nom": nom,
        "prenom": prenom,
        "age": age,
        "courriel": courriel,
        "telephone": telephone,
        "adresse": adresse,
        "codePostale": codePostale,
        "ville": ville,
        "pays": pays,
        "licence": licence,
        "classement": classement,
    }
    numeroInscription = collection.insert_one(document).inserted_id
    db.seDeconnecter()


