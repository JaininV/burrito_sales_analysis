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
        query = "INSERT INTO employe (name, role, salary_hourly) VALUES (%s, %s, %s)"
        value = (name, position, salary_hr)
        cursor.close()
        connection.close()
        return 'Data added'
    
    else:
        return 'Employe already working'
