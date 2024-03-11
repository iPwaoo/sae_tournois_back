# services/database.py
import os

from pymongo import MongoClient


class DatabaseService:
    def __init__(self):
        uri = "mongodb://localhost:27017/"
        dbname = "iut"
        self.client = MongoClient(uri)
        self.db = self.client[dbname]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# Exemple d'utilisation :
# db_service = DatabaseService("mongodb://localhost:27017/", "nom_de_votre_base_de_donnees")
# collection = db_service.get_collection("nom_de_votre_collection")
