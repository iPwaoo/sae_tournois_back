def convertion_temps(temps_a_convertir: str):
    # Convertir le temps disponible en minutes
    heures, minutes = map(int, temps_a_convertir.split('/'))
    temps_total_minutes = heures * 60 + minutes
    return temps_total_minutes


def calcule_duree_match(nombre_de_parties: int):
    return 11*nombre_de_parties

