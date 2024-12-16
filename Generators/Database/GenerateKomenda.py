import random

import Data
from Data import *
from pandas import DataFrame

from Utils import get_period_scaled_number


# ID int
# Adres varchar(20)
# Telefon char(9)
# Rejon varchar(15)

def generate_komendy():
    NUMBER_OF_HEADQUARTERS_TO_GENERATE = int(get_period_scaled_number(NUMBER_OF_HEADQUARTERS, Data.CURRENT_PERIOD_NAME))

    total_probability = sum(REGIONS_PROBABILITY)
    normalized_probabilities = [p / total_probability for p in REGIONS_PROBABILITY]

    chosen_regions = [random.choices(REGIONS, weights=normalized_probabilities, k=1)[0] for _ in range(NUMBER_OF_HEADQUARTERS_TO_GENERATE)]

    headquarters_data = DataFrame({
        'ID': [i for i in range(NUMBER_OF_HEADQUARTERS_TO_GENERATE)],
        'Address': [f"{fake.street_address()} {chosen_regions[i]}" for i in range(NUMBER_OF_HEADQUARTERS_TO_GENERATE)],
        'Phone-number': [fake.phone_number() for _ in range(NUMBER_OF_HEADQUARTERS_TO_GENERATE)],
        'Region': chosen_regions
    })
    return headquarters_data
