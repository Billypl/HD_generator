from datetime import datetime, timedelta
import random

import pandas as pd
from pandas import DataFrame

from Data import *

# ZDARZENIE
# DateTime: dt_rozpoczęcia
# DateTime: dt_zakończenia
# String: lokalizacja
# String: opis

class ZdarzeniaMassGenerator:
    def __init__(self, startDate, endDate, zdarzeniaPerDay):
        self.startPeriodDate = startDate
        self.endPeriodDate = endDate
        self.zdarzeniaPerDay = zdarzeniaPerDay
        self.zdarzenieGenerator = ZdarzenieGenerator()
        self.csv = None
        self.startDates = list()
        self.endDates = list()
        self.locations = list()
        self.descriptions = list()
        self.ids = list()

    def generate_zdarzenia(self):
        periodDateDifference = self.endPeriodDate - self.startPeriodDate
        self.template_generate_zdarzenia_data(self.generate_dates_lambda)
        self.template_generate_zdarzenia_data(self.generate_location_lambda)
        self.template_generate_zdarzenia_data(self.generate_description_lambda)
        self.csv = pd.DataFrame({
            'StartDate': self.startDates,
            'EndDate': self.endDates,
            'Location': self.locations,
            'Description': self.descriptions,
            'ID': list(range(periodDateDifference.days * self.zdarzeniaPerDay))
        })
        # self.csv = self.csv.sort_values(by='StartDate')
        return self.csv

    def template_generate_zdarzenia_data(self, action):
        periodDateDifference = self.endPeriodDate - self.startPeriodDate
        for i in range(periodDateDifference.days):
            for j in range(self.zdarzeniaPerDay):
                index = i * self.zdarzeniaPerDay + j
                action(index, i, j)

    def generate_dates_lambda(self, index, i, j):
        offsettedDate = self.startPeriodDate + timedelta(days=i)
        startDate, endDate = self.zdarzenieGenerator.generate_start_end_date_time(offsettedDate)
        self.startDates.append(startDate)
        self.endDates.append(endDate)

    def generate_location_lambda(self, index, i, j):
        self.locations.append(self.zdarzenieGenerator.generate_location())

    def generate_description_lambda(self, index, i, j):
        self.descriptions.append(self.zdarzenieGenerator.generate_description())

class ZdarzenieGenerator:

    shiftLength = 6

    def generate_zdarzenie(self):
        # self.generate_start_end_date_time()
        pass
        # return zdarzeniaTable

    def generate_start_end_date_time(self, date):
        startDateTime = date + timedelta(hours=random.randint(0, self.shiftLength), minutes=random.randint(0, 59))
        endDateTime = date + timedelta(hours=random.randint(0, self.shiftLength), minutes=random.randint(0, 59))
        if startDateTime > endDateTime:
            startDateTime, endDateTime = endDateTime, startDateTime
        return startDateTime, endDateTime

    def generate_location(self):
        adress = ""
        adress += fake.city()
        adress += "#"
        adress += fake.street_name()
        adress += "#"
        adress += fake.building_number()
        return adress.replace('\n', ' ')

    def generate_description(self):
        return random.choice(TYPES_OF_EVENTS)

# if __name__ == '__main__':
#     # TEST
#     zdarzeniaPerDay = 3
#     T1startPeriodDate = datetime(2022, 1, 1, 0, 0)
#     T1endPeriodDate = datetime(2022, 3, 30, 23, 59)
#
#     T2startPeriodDate = datetime(2022, 4, 1, 0, 0)
#     T2endPeriodDate = datetime(2022, 4, 29, 23, 59)
#
#     generator1 = ZdarzeniaMassGenerator(T1startPeriodDate, T1endPeriodDate, zdarzeniaPerDay)
#     zdarzenia = generator1.generate_zdarzenia()
#
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.width', 1000)
#     pd.set_option('display.max_columns', None)
#     print(zdarzenia)

