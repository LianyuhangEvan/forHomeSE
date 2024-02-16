import mysql.connector

config = {
    'user': 'subtle-chimera-414016:us-central1:evanse ',
    'password': '2686336654lyh',
    'host': '35.223.28.98',
    'database': 'mytestforstoring',
    'raise_on_warnings': True
}

try:
    cnx = mysql.connector.connect(**config)
    print("Connected to database")
except mysql.connector.Error as err:
    print(f"Failed to connect to database: {err}")