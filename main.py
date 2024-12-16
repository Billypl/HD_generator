import sys

import pandas as pd

import Data
from Generators.Database.GeneratePolicjanciDanegoDnia import generate_policjanci_danego_dnia
from Generators.Database.GeneratePunkty import generate_punkty
from Generators.Database.GenerateTrasa import generate_trasy
from Generators.Database.GenerateZdarzenie import ZdarzeniaMassGenerator as zdarzeniaGenerator
from Data import *

from Generators.Database.GenerateKomenda import generate_komendy
from Generators.Database.GeneratePatrol import generate_partole
from Generators.Database.GeneratePojazdy import generate_pojazdy
from Generators.Excel.GenerateAwarie import generate_awarie
from Generators.Excel.GeneratePolicjanci import generate_policjanci
from Utils import split_dataframe, split_points_dataframe, get_period_percantage, get_period_dates, get_period_length_in_days, get_period_scaled_number

# Komenda policji (Nazwa, Adres, Telefon, Rejon)
# Patrol (ID, Status, Data, Numer_rejestracyjny_pojazdu REF Pojazd)
# Policjant (danego dnia) (PESEL, ID_patrolu REF Patrol)
# Pojazd (Numer_rejestracyjny, Typ, Stan_techniczny, Spalanie, Rok_produkcji, Przebyte_kilometry, Marka, Model)
# Punkty (Numer, ID_trasy REF Trasa, Szerokość, Wysokość, Czas)
# Trasa (ID, ID_zdarzenia REF Zdarzenie)
# Zdarzenie (ID, DataCzas_rozpoczęcia , DataCzas_zakończenia, Lokalizacja, Opis)

##### non-changable
    # pojazdy ✓
    # komendy ✓
    # policjanci ✓

##### changable
    # awarie - stała liczba ✓
    # patrol - stała liczba ✓
    # zdarzenia - stała liczba (ale wymnożona przez dni!!) ✓
    # trasa - stała liczba (ale wymnożona przez dni!!)
    # punkty - RANDOM (ale na podstawie liczby tras?)
    # policjanci na patrolu - stała liczba ✓

if __name__ == '__main__':
    # print(get_period_dates("T1"))
    # print(get_period_length_in_days("T1"))
    # print(get_period_length_in_days("T"))
    # print(get_period_percantage("T2"))
    # print(get_period_scaled_number(25.3, "T1"))
    #
    # sys.exit()
#region comment
############### NEW ######################################
    # pojazd -  awarie
    #        \
    #         -> patrol
    #        /      \
    # komendy        \
    #                 \
    # zdarzenia       /\
    #      |    \    v  \
    #      |     trasy   \
    #      v    /         \
    # punkty  <-          /
    #                    /
    # policjanci        /
    #           \      /
    #            v    /
    # policjanci danego dnia

### PODSUMOWANIE
    # carefree: pojazd, komendy, zdarzenia, policjanci
    # dependent: awarie
    # double-dependent: patrol
    # deeply nested dependent: trasy, policjanci danego dnia
    # ultra nested dependent: punkty,

# t1 -> t2
# liczą się w t2: pojazd, komendy, policjanci
# reszta nah (a nawet nie powinny, bo np. nie powinno się dodawać punktów do już instiejących trash)
#endregion

##################### T1

    vehicle_data1 = generate_pojazdy()
    # print(vehicle_data1)
    damaged_vehicles_data1 = generate_awarie(vehicle_data1)
    # print(damaged_vehicles_data1)
    headquarters_data1 = generate_komendy()
    # print(headquarters_data1)
    patrol_data1 = generate_partole(headquarters_data1, vehicle_data1)
    # print(patrol_data1)
    zdarzenia_data1 = zdarzeniaGenerator(*get_period_dates(Data.CURRENT_PERIOD_NAME), ZDARZENIA_PER_DAY).generate_zdarzenia()
    # print(zdarzenia_data1)
    route_data1 = generate_trasy(zdarzenia_data1, patrol_data1, 0)
    # print(route_data1)
    points_data1 = generate_punkty(route_data1, zdarzenia_data1)
    # print(points_data1)

    policemen_data1 = generate_policjanci()
    print(policemen_data1)
    policemen_on_patrol_data1 = generate_policjanci_danego_dnia(patrol_data1, policemen_data1)
    print(policemen_on_patrol_data1)

##################### T2

    Data.CURRENT_PERIOD_NAME = "T2"

# carefree
    vehicle_data2 = generate_pojazdy()
    vehicle_data = pd.concat([vehicle_data1, vehicle_data2], ignore_index=True)
    # print(vehicle_data2)
    damaged_vehicles_data2 = generate_awarie(vehicle_data)
    # print(damaged_vehicles_data2)

    headquarters_data2 = generate_komendy()
    headquarters_data = pd.concat([headquarters_data1, headquarters_data2], ignore_index=True)
    # print(headquarters_data2)

    patrol_data2 = generate_partole(headquarters_data, vehicle_data)
    # print(patrol_data2)

# dependent
    zdarzenia_data2 = zdarzeniaGenerator(*get_period_dates(Data.CURRENT_PERIOD_NAME), ZDARZENIA_PER_DAY).generate_zdarzenia()
    # print(zdarzenia_data2)
    route_data2 = generate_trasy(zdarzenia_data2, patrol_data2, len(route_data1))
    # print(route_data1)
    points_data2 = generate_punkty(route_data2, zdarzenia_data2)
    # print(points_data1)

    policemen_data2 = generate_policjanci()
    policemen_data = pd.concat([policemen_data1, policemen_data2], ignore_index=True)
    print(policemen_data2)
    policemen_on_patrol_data2 = generate_policjanci_danego_dnia(patrol_data2, policemen_data)
    print(policemen_on_patrol_data2)



######################################
##########  ZAPISYWANIE1   ###########
######################################

    vehicle_data1.to_csv('GeneratedOutput1/Pojazd.bulk', sep='|', index=False)
    headquarters_data1.to_csv('GeneratedOutput1/Komenda_policji.bulk', sep='|', index=False)
    policemen_data1.to_csv('GeneratedOutput1/Policjanci.bulk', sep='|', index=False)

    vehicle_data2.to_csv('GeneratedOutput2/Pojazd.bulk', sep='|', index=False)
    headquarters_data2.to_csv('GeneratedOutput2/Komenda_policji.bulk', sep='|', index=False)
    policemen_data2.to_csv('GeneratedOutput2/Policjanci.bulk', sep='|', index=False)

######################################
##########    DZIELENIE    ###########
######################################

    # t1_patrol_data, t2_patrol_data = split_dataframe(patrol_data1, int(NUMBER_OF_PATROLS * 2 / 3))
    # t1_policemen_on_patrol_data, t2_policemen_on_patrol_data = split_dataframe(policemen_on_patrol_data1, int(NUMBER_OF_POLICEMEN_ON_PATROL * 2 / 3))
    #
    # periodDateDifference = (T1_START_PERIOD_DATE - T1_END_PERIOD_DATE).days
    #
    # t1_zdarzenia_data, t2_zdarzenia_data = split_dataframe(zdarzenia_data1, int(ZDARZENIA_PER_DAY * periodDateDifference * 1 / 3))
    # t1_route_data, t2_route_data = split_dataframe(route_data1, int(ZDARZENIA_PER_DAY * periodDateDifference * 1 / 3))
    # t1_damaged_vehicles_data, t2_damaged_vehicles_data = split_dataframe(damaged_vehicles_data1, int(NUMBER_OF_DAMAGES * 2 / 3))
    # t1_points_data, t2_points_data = split_points_dataframe(points_data1, int(len(route_data1) * 2 / 3))
    #
    # vehicle_data1.to_csv('GeneratedOutput1/Pojazd.bulk', sep='|', index=False)
    # headquarters_data1.to_csv('GeneratedOutput1/Komenda_policji.bulk', sep='|', index=False)
    # policemen_data1.to_csv('GeneratedOutput1/Policjanci.bulk', sep='|', index=False)

######################################
##########  ZAPISYWANIE1   ###########
######################################

    damaged_vehicles_data1.to_csv('GeneratedOutput1/Awarie.bulk', sep='|', index=False)
    patrol_data1.to_csv('GeneratedOutput1/Patrol.bulk', sep='|', index=False)
    zdarzenia_data1.to_csv('GeneratedOutput1/Zdarzenie.bulk', sep='|', index=False)
    route_data1.to_csv('GeneratedOutput1/Trasa.bulk', sep='|', index=False)
    points_data1.to_csv('GeneratedOutput1/Punkty.bulk', sep='|', index=False)

    policemen_on_patrol_data1.to_csv('GeneratedOutput1/Policjant_danego_dnia.bulk', sep='|', index=False)

######################################
##########  ZAPISYWANIE2   ###########
######################################

    damaged_vehicles_data2.to_csv('GeneratedOutput2/Awarie.bulk', sep='|', index=False)
    patrol_data2.to_csv('GeneratedOutput2/Patrol.bulk', sep='|', index=False)
    zdarzenia_data2.to_csv('GeneratedOutput2/Zdarzenie.bulk', sep='|', index=False)
    route_data2.to_csv('GeneratedOutput2/Trasa.bulk', sep='|', index=False)
    points_data2.to_csv('GeneratedOutput2/Punkty.bulk', sep='|', index=False)

    policemen_on_patrol_data2.to_csv('GeneratedOutput2/Policjant_danego_dnia.bulk', sep='|', index=False)
