from flask import Blueprint, request, jsonify
from services.algorithmes.tournois import tournois_recherche
from services.algorithmes.tournois import tournois_modification
from services.algorithmes.tournois import tournois_insertion

tournois_bp = Blueprint('tournois', __name__)


@tournois_bp.route('/', methods=['GET'])
def get_all():
    result = tournois_recherche.tout_les_tournois()
    return jsonify(result)


@tournois_bp.route('/<string:tournois_name>', methods=['GET'])
def get_by_name(tournois_name):
    result = tournois_recherche.recherche_tournois(tournois_name)
    return jsonify(result)


@tournois_bp.route('/', methods=['POST'])
def add_tournois():
    nom = request.json.get('nom')
    prenom = request.json.get('prenom')
    sexe = request.json.get('sexe')
    categorie = request.json.get('categorie')
    print(categorie)
    tournois_insertion.insertion_tournois(nom, prenom, sexe, categorie)
    return f"Tu as ajouté dans le fichier : {request.json}"


@tournois_bp.route('/', methods=['PUT'])
def update_tournois():
    modification = request.json
    id_tournois = modification.get('_id')  # Supposons que l'identifiant soit fourni dans le document JSON
    document_modification = modification.get('modification')  # Supposons que les modifications soient fournies dans un champ "modification" dans le JSON
    if not id_tournois:
        return jsonify({"error": "L'identifiant du tournois est manquant"})
    if not document_modification:
        return jsonify({"error": "Les données de modification sont manquantes"})
    tournois_modification.modifier_tournois(id_tournois, document_modification)
    return jsonify({"message": "tournois mis à jour avec succès"})
