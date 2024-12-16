from datetime import datetime
from faker import Faker

T1_START_PERIOD_DATE = datetime(2022, 1, 1, 0, 0)
T1_END_PERIOD_DATE = datetime(2022, 3, 31, 23, 59)
T2_START_PERIOD_DATE = datetime(2022, 4, 1, 0, 0)
T2_END_PERIOD_DATE = datetime(2022, 4, 30, 23, 59)

CURRENT_PERIOD_NAME = "T1"

fake = Faker("pl_PL")

# ZDARZENIA
ZDARZENIA_PER_DAY = 500 # 3
TYPES_OF_EVENTS = ['kradzież', 'włamanie', 'zakłócanie porządku', 'wypadek drogowy', 'bójka']

# AWARIE
NUMBER_OF_DAMAGES = 120_000
TYPES_OF_DAMAGE = ['Silnik', 'Szyba', 'Opona', 'Elektronika', 'Zawieszenie', 'Skrzynia biegów', 'Wgniecenie', 'Hamulce']

# PATROL
POLICEMEN_NUMBER_ON_PATROL = 2
NUMBER_OF_PATROLS = 100_000 # 1500
# policjanci/2 * komendy * dni
# 1000 * 50 * 90 = 4 500 000
STATUS = ['aktywny', 'zajęty', 'nieaktywny']
PROBABILITY_OF_STATUS = [0.45, 0.45, 0.1]

# POLICJANCI
NUMBER_OF_POLICEMEN = 50_000 # 2000
RANKS = [
    "GENERALNY INSPEKTOR", "NADINSPEKTOR", "INSPEKTOR", "MŁODSZY INSPEKTOR",
    "PODINSPEKTOR", "NADKOMISARZ", "KOMISARZ", "PODKOMISARZ",
    "ASPIRANT SZTABOWY", "STARSZY ASPIRANT", "ASPIRANT", "MŁODSZY ASPIRANT",
    "SIERŻANT SZTABOWY", "STARSZY SIERŻANT", "SIERŻANT",
    "STARSZY POSTERUNKOWY", "POSTERUNKOWY"
]

# POLICJANCI DANEGO DNIA
# NUMBER_OF_POLICEMEN_ON_PATROL = NUMBER_OF_POLICEMEN

# KOMENDA
NUMBER_OF_HEADQUARTERS = 50
REGIONS = [
    'Gdańsk','Gdynia','Sopot',
    'Słupsk','Tczew','Wejherowo',
    'Malbork','Starogard Gdański','Puck',
    'Kartuzy','Lębork','Pruszcz Gdański',
    'Reda','Rumia','Nowy Dwór Gdański',
    'Chojnice','Bytów','Czersk',
    'Kościerzyna','Dziwnów','Powiat gdański',
    'Powiat pucki','Powiat słupski',
    'Powiat tczewski','Powiat wejherowski',
    'Powiat starogardzki','Powiat bytowski','Powiat lęborski',
    'Powiat kościerski','Powiat nowodworski','Powiat chojnicki'
]
# Miasta (20 pierwszych rekordow regions) maja wieksze prawdopodobienstwo niz powiaty
REGIONS_PROBABILITY = [5] * 20 + [1] * (len(REGIONS) - 20)

# POJAZDY
NUMBER_OF_VEHICLES = 60_000
MODELS = [
    'Clio', 'Sandero', 'Arkana', 'Mazda2', 'Express', 'Dokker', 'Master',
    'Golf', 'Passat', 'Octavia', 'Fabia', 'Focus', 'Fiesta', 'Civic',
    'Accord', 'A4', 'A6', '3 Series', 'X3', 'C-Class', 'E-Class',
    'Tiguan', 'Qashqai', 'Santa Fe', 'Kuga', 'Captur', 'Koleos',
    'Duster', 'Niro', 'Soul', 'Seltos', 'Corolla', 'Camry', 'RAV4'
]
BRANDS = {
    'RENAULT': ['Clio', 'Arkana', 'Express', 'Master', 'Captur', 'Koleos'],
    'TOYOTA': ['RAV4', 'Camry', 'Corolla'],
    'KIA': ['Niro', 'Soul', 'Seltos'],
    'DACIA': ['Sandero', 'Dokker', 'Duster'],
    'MAZDA': ['Mazda2'],
    'VOLKSWAGEN': ['Golf', 'Passat', 'Tiguan'],
    'SKODA': ['Octavia', 'Fabia'],
    'FORD': ['Focus', 'Fiesta', 'Kuga'],
    'HONDA': ['Civic', 'Accord'],
    'AUDI': ['A4', 'A6'],
    'BMW': ['3 Series', 'X3'],
    'MERCEDES': ['C-Class', 'E-Class'],
    'NISSAN': ['Qashqai'],
    'HYUNDAI': ['Santa Fe'],
}
HELICOPTER_MODELS = [
    '206',
    '407',
    'S-76',
    'UH-60 Black Hawk',
    'AS350',
    'AW139',
    'R44'
]
HELICOPTER_BRANDS = {
    'Bell': ['206', '407'],
    'Sikorsky': ['S-76', 'UH-60 Black Hawk'],
    'Eurocopter': ['AS350', 'AW139']
}

TYPES = ['Radiowóz', 'Motor', 'Helikopter', 'Skuter wodny']
CONDITION = ['zdatny', 'w naprawie', 'niezdatny']
PROBABILITY = [0.8, 0.15, 0.05]


# ZDARZENIA 3800 * 4 * 30 = 445 000
# PUNKTY
# (20<->500) * 3800 * 4*30 = NUMBER_OF_POINTS = 8 900 000 <-> 222 500 000
# 100 * 90dni * 15
# NUMBER_OF_POINTS = 100_000 # 10000
POINT_SNAPSHOT_FREQUENCY_MIN = 2 # 10
MIN_NUMBER_OF_POINTS_IN_ROUTE = 10 # 2
MAX_NUMBER_OF_POINTS_IN_ROUTE = 30 # 50
MAX_DISTANCE_KM = 5