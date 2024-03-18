from services.connexion.DatabaseService import DatabaseService


def modifier_nom_joueur(id_joueur: str, nouveau_nom: str):
    db = DatabaseService()
    collection = db.get_collection("joueur")
    filtre = {"_id": id_joueur}
    mise_a_jour = {"$set": {"nom": nouveau_nom}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_prenom_joueur(id_joueur: str, nouveau_prenom: str):
    db = DatabaseService()
    collection = db.get_collection("joueur")
    filtre = {"_id": id_joueur}
    mise_a_jour = {"$set": {"prenom": nouveau_prenom}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_categorie_joueur(id_joueur: str, nouvelle_categorie: {int, str}):
    db = DatabaseService()
    collection = db.get_collection("joueur")
    filtre = {"_id": id_joueur}
    mise_a_jour = {"$set": {
        "categorie": {
            "age": nouvelle_categorie[0],
            "niveau": nouvelle_categorie[1]
        }
    }}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()
