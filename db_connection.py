import mysql.connector

config = {
    'user': 'root',
    'password': 'Jainin@0511',
    'host': 'localhost',
    'database': 'fbb_database'
}

try:
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(buffered=True)

except mysql.connector.Error as err:
    print(err)

    


