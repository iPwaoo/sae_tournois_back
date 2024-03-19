from bson import ObjectId
from services.connexion.DatabaseService import DatabaseService


def modifier_nb_table(id_tournoi: str, nouveau_nb_table: int):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"_id": ObjectId(id_tournoi)}
    mise_a_jour = {"$set": {"nbTable": nouveau_nb_table}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_duree_max(id_tournoi: str, nouvelle_duree_max: int):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"_id": ObjectId(id_tournoi)}
    mise_a_jour = {"$set": {"dureeMax": nouvelle_duree_max}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_date(id_tournoi: str, nouvelle_date: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"_id": ObjectId(id_tournoi)}
    mise_a_jour = {"$set": {"date": nouvelle_date}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_lieu(id_tournoi: str, nouveau_nom_lieu: str, nouvelle_capacite: int, nouvelle_adresse_nom: str,
                  nouvelle_adresse_rue: str, nouvelle_adresse_code_postal: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"_id": ObjectId(id_tournoi)}
    mise_a_jour = {
        "$set": {
            "lieu.nom": nouveau_nom_lieu,
            "lieu.capacite": nouvelle_capacite,
            "lieu.adresse.nom": nouvelle_adresse_nom,
            "lieu.adresse.rue": nouvelle_adresse_rue,
            "lieu.adresse.codePostale": nouvelle_adresse_code_postal
        }
    }
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_objectif(id_tournoi: str, nouvel_objectif: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"_id": ObjectId(id_tournoi)}
    mise_a_jour = {"$set": {"objectif": nouvel_objectif}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()


def modifier_format(id_tournoi: str, nouveau_format: str):
    db = DatabaseService()
    collection = db.get_collection("tournois")
    filtre = {"_id": ObjectId(id_tournoi)}
    mise_a_jour = {"$set": {"format": nouveau_format}}
    collection.update_one(filtre, mise_a_jour)
    db.seDeconnecter()
