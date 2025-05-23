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
    f_name = data['first_name']
    l_name = data['last_name']
    position = data['role']
    salary_hr = data['salary_hourly']
    email = data['email_id']
    phone_number = data['phone_number']
    address = data['address']
    postal = data['postal_code']


    cursor.execute("SELECT * FROM employe WHERE first_name = %s AND last_name = %s AND active = %s", (f_name, l_name, 1))
    check = cursor.fetchone()
    connection.commit()

    if check is None:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        query = "INSERT INTO employe (first_name, last_name, role, salary_hourly, email_id, phone_number, address, postal_code, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (f_name, l_name, position, salary_hr, email, phone_number, address, postal, formatted_datetime, formatted_datetime)

        cursor.execute(query, value)
        connection.commit()
        cursor.close()
        connection.close()

        return "asdasdas"
        # try:
        #     cursor.execute(query, value)
        #     connection.commit()
        #     cursor.close()
        #     connection.close()

        #     return 'Data added'
        
        # except Exception as e:
        #     return f"Error: {str(e)}"
    
    else:
        return 'Employe already working'
