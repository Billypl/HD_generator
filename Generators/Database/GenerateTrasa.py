# Trasa (ID, ID_zdarzenia REF Zdarzenie, ID_patrolu REF Patrol)
import random

from pandas import DataFrame
from Utils import rand_value_from_column


def generate_trasy(zdarzenia_data, patrol_data, start_id):
    trasy = DataFrame(columns=['ID', 'ID_zdarzenia', 'ID_patrolu'])
    trasy['ID_zdarzenia'] = zdarzenia_data['ID']
    trasy['ID'] = [i for i in range(start_id, len(zdarzenia_data) + start_id)]
    trasy['ID_patrolu'] = [rand_value_from_column(column=patrol_data['ID']) for _ in range(len(zdarzenia_data))]
    return trasy
