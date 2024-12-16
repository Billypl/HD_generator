import Data
from Data import *
from Utils import *

# PESEL FK
# ID_PATROLU FK


def generate_policjanci_danego_dnia(patrol_data, policemen_data):
    assigned_pairs = list()
    for i in range(len(patrol_data)):
        patrol_id = patrol_data['ID'].iloc[i]
        policemens_id = []
        for j in range(POLICEMEN_NUMBER_ON_PATROL):
            pesel = rand_value_from_column(column=policemen_data['PESEL'])
            while pesel in policemens_id:
                pesel = rand_value_from_column(column=policemen_data['PESEL'])
            policemens_id.append(pesel)
            assigned_pairs.append((pesel, patrol_id))

    policemen_on_patrol_data = pd.DataFrame(assigned_pairs, columns=['PESEL', 'ID_patrolu'])
    return policemen_on_patrol_data

