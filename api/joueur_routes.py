from flask import Blueprint, request, jsonify
from services.algorithmes.joueur import joueur_recherche
from services.algorithmes.joueur import joueur_modification
from services.algorithmes.joueur import joueur_insertion

joueur_bp = Blueprint('joueur', __name__)


@joueur_bp.route('/', methods=['GET'])
def get_all():
    result = joueur_recherche.tout_les_joueurs()
    return jsonify(result)


@joueur_bp.route('/<string:joueurs_name>', methods=['GET'])
def get_by_name(joueurs_name):
    result = joueur_recherche.recherche_joueur(joueurs_name)
    return jsonify(result)


@joueur_bp.route('/', methods=['POST'])
def add_joueur():
    print(request.json)
    nom = request.json.get('nom')
    prenom = request.json.get('prenom')
    sexe = request.json.get('sexe')
    categorie = request.json.get('categorie')
    print(categorie)
    #joueur_insertion.insertion_joueur(nom, prenom, sexe, categorie)
    return f"Tu as ajouté dans le fichier : {request.json}"


@joueur_bp.route('/', methods=['PUT'])
def update_joueur():
    modification = request.json
    id_joueur = modification.get('_id')  # Supposons que l'identifiant soit fourni dans le document JSON
    document_modification = modification.get('modification')  # Supposons que les modifications soient fournies dans un champ "modification" dans le JSON
    if not id_joueur:
        return jsonify({"error": "L'identifiant du joueur est manquant"})
    if not document_modification:
        return jsonify({"error": "Les données de modification sont manquantes"})
    joueur_modification.modifier_joueur(id_joueur, document_modification)
    return jsonify({"message": "Joueur mis à jour avec succès"})
