from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
import datetime
import json

# Simulated async function
def getEmployeDataApi():
    query = "SELECT * FROM employe"

    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()

    return {
        'data': result
    }

# add values in employe
def addEmployeDataApi(data):
    cursor = connection.cursor()
    name = data['name']
    position = data['role']
    salary_hr = data['salary_hourly']

    cursor.execute("SELECT * FROM employe WHERE name = %s AND active = %s", (name, 1))
    check = cursor.fetchone()
    connection.commit()

    if check is None:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        query = "INSERT INTO employe (name, role, salary_hourly, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
        value = (name, position, salary_hr, formatted_datetime, formatted_datetime)

        cursor.close()
        connection.close()
        return 'Data added'
    
    else:
        return 'Employe already working'
