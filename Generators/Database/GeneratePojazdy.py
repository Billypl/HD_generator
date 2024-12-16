import random
import string

import Data
from Data import *
from pandas import DataFrame

from Utils import get_period_scaled_number


# Numer_rejestracyjny K
# Typ
# Stan_techniczny
# Spalanie
# Rok_produkcji
# Przebyte_kilometry
# Marka
# Model

def generate_registration_number():
    registration_number = ''.join(random.choices(string.ascii_uppercase, k=2)) + ' ' + \
                          ''.join(random.choices(string.digits, k=4))
    return registration_number

def generate_registration_numbers(NUMBER_OF_VEHICLES_TO_GENERATE):
    registration_numbers = list()
    while len(registration_numbers) < NUMBER_OF_VEHICLES_TO_GENERATE:
        registration_number = generate_registration_number()
        while registration_number in registration_numbers:
            registration_number = generate_registration_number()
        registration_numbers.append(registration_number)
    return registration_numbers

def correct_helicopters_data(vehicle_data):
    NUMBER_OF_VEHICLES_TO_GENERATE = int(get_period_scaled_number(NUMBER_OF_VEHICLES, Data.CURRENT_PERIOD_NAME))
    for i in range(NUMBER_OF_VEHICLES_TO_GENERATE):
        if vehicle_data['Type'][i] == 'Helikopter':
            vehicle_data['Combustion'][i] = round(random.uniform(20.0, 100.0), 2)
            selected_brand = random.choice(list(HELICOPTER_BRANDS.keys()))
            vehicle_data['Brand'][i] = selected_brand
            vehicle_data['Model'][i] = random.choice(HELICOPTER_BRANDS[selected_brand])

def generate_pojazdy():
    print(Data.CURRENT_PERIOD_NAME)
    NUMBER_OF_VEHICLES_TO_GENERATE = int(get_period_scaled_number(NUMBER_OF_VEHICLES, Data.CURRENT_PERIOD_NAME))

    registration_numbers = generate_registration_numbers(NUMBER_OF_VEHICLES_TO_GENERATE)
    list_of_models = list()
    list_of_brands = list()

    for i in range(NUMBER_OF_VEHICLES_TO_GENERATE):
        brand = random.choice(list(BRANDS.keys()))
        model = random.choice(BRANDS[brand])
        list_of_brands.append(brand)
        list_of_models.append(model)

    vehicle_data = {
        'Registration-number': list(registration_numbers),
        'Type': [random.choice(TYPES) for _ in range(NUMBER_OF_VEHICLES_TO_GENERATE)],
        'Technical-condition': [random.choices(CONDITION, weights=PROBABILITY, k=1)[0] for _ in range(NUMBER_OF_VEHICLES_TO_GENERATE)],
        'Combustion': [round(random.uniform(4.0, 15.0), 2) for _ in range(NUMBER_OF_VEHICLES_TO_GENERATE)],
        'Production-year': [random.randint(2000, 2018) for _ in range(NUMBER_OF_VEHICLES_TO_GENERATE)],
        'Kilometers-traveled': [random.randint(0, 200000) for _ in range(NUMBER_OF_VEHICLES_TO_GENERATE)],
        'Brand': list(list_of_brands),
        'Model': list(list_of_models)
    }

    correct_helicopters_data(vehicle_data)
    vehicle_data = DataFrame(vehicle_data)
    return vehicle_data
