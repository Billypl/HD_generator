# Punkty (Numer, ID_trasy REF Trasa, Szerokość, Wysokość, Czas)
from numpy import datetime64

from Utils import *
from Data import *
from geopy.distance import geodesic

def generate_next_time(start, minutes=0):
    if isinstance(start, datetime64):
        start = pd.to_datetime(start).to_pydatetime()
    next_time = start + timedelta(minutes=minutes)
    return next_time

def find_zdarzenie(id_trasy, route_data, zdarzenia_data):
    id_zdarzenia = route_data[route_data['ID'] == id_trasy]['ID_zdarzenia'].values[0]
    return zdarzenia_data[zdarzenia_data['ID'] == id_zdarzenia]


def generate_punkty(route_data, zdarzenia_data):
    # Lists for accumulating points data
    point_numbers = []
    routs_ids = []
    latitudes = []
    longitudes = []
    timestamps = []

    # Dictionary to store the start timestamps for each route
    routs_timestamps_dict = {}

    for i in range(len(route_data)):
        if i % 1000 == 0:
            print(i)
        points_amount_in_route = random.randint(MIN_NUMBER_OF_POINTS_IN_ROUTE, MAX_NUMBER_OF_POINTS_IN_ROUTE)
        id_trasy = route_data.loc[i, 'ID']

        # Get the start timestamp for the route
        if id_trasy not in routs_timestamps_dict:
            zdarzenie_start_time = find_zdarzenie(id_trasy, route_data, zdarzenia_data)['StartDate'].iloc[0]
            routs_timestamps_dict[id_trasy] = zdarzenie_start_time
            current_timestamp = zdarzenie_start_time
        else:
            current_timestamp = routs_timestamps_dict[id_trasy]


        # Generate random points for the route
        for j in range(points_amount_in_route):
            routs_ids.append(id_trasy)
            point_numbers.append(j)
            timestamps.append(current_timestamp)

            if j == 0:
                latitudes.append(fake.latitude())
                longitudes.append(fake.longitude())
            else:
                # Losowy kierunek i odległość
                offset_km = random.uniform(0, MAX_DISTANCE_KM)  # odległość w km
                bearing = random.uniform(0, 360)  # losowy kierunek w stopniach

                # Obliczanie nowego punktu
                new_location = geodesic(kilometers=offset_km).destination((latitudes[-1], longitudes[-1]), bearing)
                new_latitude, new_longitude = new_location.latitude, new_location.longitude
                latitudes.append(new_latitude)
                longitudes.append(new_longitude)

            # Generate the next timestamp for subsequent points
            current_timestamp = generate_next_time(current_timestamp, POINT_SNAPSHOT_FREQUENCY_MIN)

    # Create DataFrame once all data is collected
    points_data = pd.DataFrame({
        'Numer': point_numbers,
        'ID_trasy': routs_ids,
        'Szerokość': latitudes,
        'Wysokość': longitudes,
        'Czas': timestamps
    })

    return points_data
