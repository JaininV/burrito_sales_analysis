import mysql.connector

config = {
    'user': 'root',
    'password': 'Jainin@0511',
    'host': 'localhost',
    'database': 'fbb_database'
}

def database_connection(config):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(buffered=True)
        return "database connected!"
    except mysql.connector.Error as err:
        return err

database_connection(config)
