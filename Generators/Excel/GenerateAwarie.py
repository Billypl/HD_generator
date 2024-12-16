import random
from pandas import DataFrame

import Data
from Utils import rand_date, rand_value_from_column, get_period_scaled_number, get_period_dates
from Data import *

# Column A - Numer rejestracyjny (varchar(8))
# Column B - Uszkodzenie (enum(Silnik, Szyba, Opona, Elektronika, Zawieszenie, Skrzynia biegów, Wgniecenie, Hamulce))
# Column C - Czas (datetime)


def generate_unique_dates(NUMBER_OF_DAMAGES_TO_GENERATE, vehicle_data):
    dates_set = set()
    for _ in range(NUMBER_OF_DAMAGES_TO_GENERATE):
        while True:
            rng_date = choose_damage_date(*get_period_dates(Data.CURRENT_PERIOD_NAME), vehicle_data)
            if rng_date not in dates_set:
                break
        dates_set.add(rng_date)
    return list(dates_set)

def choose_damage_date(start_date, end_date, vehicle_data):
    NUMBER_OF_VEHICLES_TO_GENERATE = int(get_period_scaled_number(NUMBER_OF_VEHICLES, Data.CURRENT_PERIOD_NAME))
    random_index = random.randint(0, NUMBER_OF_VEHICLES_TO_GENERATE - 1)
    production_year = vehicle_data.loc[random_index, 'Production-year']
    production_date = datetime(year=production_year, month=1, day=1)
    chosen_date = rand_date(max(production_date, start_date), end_date)
    return chosen_date

# im pozniej tym mniej awarii? - tendencja
def generate_awarie(vehicle_data):
    NUMBER_OF_DAMAGES_TO_GENERATE = int(get_period_scaled_number(NUMBER_OF_DAMAGES, Data.CURRENT_PERIOD_NAME))
    NUMBER_OF_DAMAGES_ALREADY_GENERATED = 0 if Data.CURRENT_PERIOD_NAME == "T1" else int(get_period_scaled_number(NUMBER_OF_DAMAGES, "T1"))
    damaged_vehicles = list()

    while len(damaged_vehicles) < NUMBER_OF_DAMAGES_TO_GENERATE:
        damaged_vehicles.append(rand_value_from_column(column=vehicle_data['Registration-number']))

    damaged_vehicles_data = DataFrame({
        'ID': [i for i in range(NUMBER_OF_DAMAGES_ALREADY_GENERATED, NUMBER_OF_DAMAGES_TO_GENERATE + NUMBER_OF_DAMAGES_ALREADY_GENERATED)],
        'Registration-Number': list(damaged_vehicles),
        'Damage': [random.choice(TYPES_OF_DAMAGE) for _ in range(NUMBER_OF_DAMAGES_TO_GENERATE)],
        'DateTime': generate_unique_dates(NUMBER_OF_DAMAGES_TO_GENERATE, vehicle_data)
    })
    return damaged_vehicles_data
