import Data
from Generators.Excel.GenerateAwarie import *
from Data import *
# ID K
# Status
# Data
# Nr rejestraycjny pojazdu FK

def generate_unique_dates(NUMBER_OF_PATROLS_TO_GENERATE):
    dates_set = set()
    for _ in range(NUMBER_OF_PATROLS_TO_GENERATE):
        while True:
            rng_date = rand_date(*get_period_dates(Data.CURRENT_PERIOD_NAME))
            if rng_date not in dates_set:
                break
        dates_set.add(rng_date)
    return list(dates_set)

# DATA
def generate_partole(headquarters_data, vehicle_data):
    NUMBER_OF_PATROLS_TO_GENERATE = int(get_period_scaled_number(NUMBER_OF_PATROLS, Data.CURRENT_PERIOD_NAME))
    NUMBER_OF_PATROLS_ALREADY_GENERATED = 0 if Data.CURRENT_PERIOD_NAME == "T1" else int(get_period_scaled_number(NUMBER_OF_PATROLS, "T1"))

    patrol_data = DataFrame({
        'ID': [i for i in range(NUMBER_OF_PATROLS_ALREADY_GENERATED, NUMBER_OF_PATROLS_TO_GENERATE + NUMBER_OF_PATROLS_ALREADY_GENERATED)],
        'Status': [random.choices(STATUS, weights=PROBABILITY_OF_STATUS, k=1)[0] for _ in range(NUMBER_OF_PATROLS_TO_GENERATE)],
        'Date': generate_unique_dates(NUMBER_OF_PATROLS_TO_GENERATE),
        'Registration-number': [rand_value_from_column(column=vehicle_data['Registration-number']) for _ in range(NUMBER_OF_PATROLS_TO_GENERATE)],
        'ID_komendy': [rand_value_from_column(column=headquarters_data['ID']) for _ in range(NUMBER_OF_PATROLS_TO_GENERATE)]
    })
    return patrol_data
