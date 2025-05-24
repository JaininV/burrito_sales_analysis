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
    user_id = "_".join([f_name, l_name])
    position = data['role']
    salary_hr = data['salary_hourly']
    email = data['email_id']
    phone_number = data['phone_number']
    address = data['address']
    postal = data['postal_code']


    cursor.execute("SELECT * FROM employe WHERE first_name = %s AND last_name = %s AND user_id = %s AND active = %s", (f_name, l_name, user_id, 1))
    check = cursor.fetchone()
    connection.commit()

    if check is None:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        query = "INSERT INTO employe (first_name, last_name, user_id, role, salary_hourly, email_id, phone_number, address, postal_code, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        value = (f_name, l_name, user_id, position, salary_hr, email, phone_number, address, postal, formatted_datetime, formatted_datetime)

        try:
            cursor.execute(query, value)
            connection.commit()
            cursor.close()
            connection.close()

            return 'Data added'
        
        except Exception as e:
            return f"Error: {str(e)}"
    
    else:
        return 'Employe already working'

def upadteEmployeDataApi(data):
    try:
        cursor = connection.cursor()
        f_name = data['first_name']
        l_name = data['last_name']
        user_id = data['user_id']
        position = data['role']
        salary_hr = data['salary_hourly']
        email = data['email_id']
        phone_number = data['phone_number']
        address = data['address']
        postal = data['postal_code']

        check_query = "SELECT * FROM employe WHERE user_id = %s"
        check_value = (user_id)
        cursor.execute(check_query, check_value)
        check_result = cursor.fetchone()

        if check_result:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            user_id = "_".join([f_name, l_name])
            query = "UPDATE employe SET first_name = %s, last_name = %s, user_id = %s, role = %s, salary_hourly = %s, email_id = %s, phone_number = %s, address = %s, postal_code = %s, updated_at = %s WHERE user_id = %s"
            value = (f_name, l_name, user_id, position, salary_hr, email, phone_number, address, postal, formatted_datetime, user_id)
            cursor.execute(query, value)
            
            return {
                'status': 'sucess',
                'message': 'Data update sucessfully'
            }
        
        else:
            return{
                'status': 'sucess',
                'message': 'Employe Not Found'
            }

    except Exception as err:
        return {
            'status': 'error',
            'message': str(err)
        }
    
    finally:
        cursor.close()
        connection.close()