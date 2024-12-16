from datetime import timedelta
from Data import *
import random

import pandas as pd

def get_period_dates(period_name):
    if period_name == "T1":
        return T1_START_PERIOD_DATE, T1_END_PERIOD_DATE
    elif period_name == "T2":
        return T2_START_PERIOD_DATE, T2_END_PERIOD_DATE
    elif period_name == "T":
        return T1_START_PERIOD_DATE, T2_END_PERIOD_DATE

def get_period_length_in_days(period_name):
    start, end = get_period_dates(period_name)
    return (end - start).days + 1

def get_period_percantage(period_name):
    return get_period_length_in_days(period_name) / get_period_length_in_days("T")

def get_period_scaled_number(variable, period_name):
    return variable * get_period_percantage(period_name)

def rand_date(min_date, max_date):
    date_difference = max_date - min_date
    return min_date + timedelta(days=random.randint(0, date_difference.days),
                                hours=random.randint(0, 23),
                                minutes=random.randint(0, 59),
                                seconds=random.randint(0, 59)
                                )

def rand_value_from_column(column):
    rng_value = column[random.randint(0, len(column) - 1)]
    return rng_value

def calculate_date_difference(startDate, endDate):
    return startDate - endDate

def generate_next_random_date(startDate, max_rand_days=0, max_rand_hours=0, max_rand_minutes=0):
   return startDate + timedelta(days=random.randint(0, max_rand_days),
                                hours=random.randint(0, max_rand_hours),
                                minutes=random.randint(0, max_rand_minutes))
def pd_debug_setup():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.max_columns', None)

def split_dataframe(df, index):
    df1 = df.iloc[:index]  # up to the index (excluding it)
    df2 = df.iloc[index:]
    return df1, df2


def split_points_dataframe(df, routes_number):
    routes_found = 0
    for index in range(len(df)):
        if df.loc[index, 'Numer'] == 0:
            routes_found += 1
        if routes_found == routes_number:
            return split_dataframe(df, index)
