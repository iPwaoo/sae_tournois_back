import services.algorithmes.nombre_participants.utils as utils


def calcul_max_participants(temps_disponible: str, nombre_de_parties: int):
    # Calculer la durée d'un match en minutes
    temps_total_minutes = utils.convertion_temps(temps_disponible)
    # Calcule duree d'un match
    duree_match = utils.calcule_duree_match(nombre_de_parties)
    # Calculer le nombre maximal de matches pouvant être joués avec le temps disponible
    max_matches = temps_total_minutes // duree_match
    # Calculer le nombre maximal de participants (chaque match implique deux participants)
    max_participants = max_matches * 2
    return max_participants