import random
from datetime import date

import Data
from Data import *
from pandas import DataFrame

from Utils import get_period_scaled_number


def generate_pesel():
    birth_date = date.fromordinal(random.randint(date(1954, 1, 1).toordinal(), date(2006, 12, 31).toordinal()))
    year = birth_date.year % 100  # the rest from division by 100
    month = birth_date.month
    day = birth_date.day

    if birth_date.year >= 2_000:
        month += 20

    random_digits = [random.randint(0, 9) for _ in range(4)]

    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_sum = sum(w * d for w, d in
                      zip(weights, [int(d) for d in f"{year:02}{month:02}{day:02}{''.join(map(str, random_digits))}"]))
    control_digit = (10 - (control_sum % 10)) % 10

    pesel = f"{year:02}{month:02}{day:02}{''.join(map(str, random_digits))}{control_digit}"
    sex = 'K'if int(pesel[10]) % 2 == 0 else 'M'

    return pesel, birth_date, sex

def generate_policjanci():
    NUMBER_OF_POLICEMEN_TO_GENERATE = int(get_period_scaled_number(NUMBER_OF_POLICEMEN, Data.CURRENT_PERIOD_NAME))
    unique_pesel = list()
    birth_days = list()
    genders = list()

    while len(unique_pesel) < NUMBER_OF_POLICEMEN_TO_GENERATE:
        pesel, birthday, sex = generate_pesel()

        if pesel not in unique_pesel:
            unique_pesel.append(pesel)
            birth_days.append(birthday)
            genders.append(sex)


    policemen_data = DataFrame({
        'Badge-number': list(unique_pesel),
        'Name': [fake.name() for _ in range(NUMBER_OF_POLICEMEN_TO_GENERATE)],
        'Surname': [fake.last_name() for _ in range(NUMBER_OF_POLICEMEN_TO_GENERATE)],
        'Date-of-birth': list(birth_days),
        'PESEL': list(unique_pesel),
        'Sex': list(genders),
        'Rank': [random.choice(RANKS) for _ in range(NUMBER_OF_POLICEMEN_TO_GENERATE)]
    })
    return policemen_data
