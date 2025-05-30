from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
import datetime
import json
import random

# Simulated async function
def getInventoryDataApi():
    query = "SELECT * FROM inventory"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    

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

            return 'Data added'
        
        except Exception as e:
            return f"Error: {str(e)}"

        finally:
            cursor.close()
            
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
        cursor.execute("SELECT * FROM employe WHERE user_id = %s AND active = %s", (user_id, 1))
        check_result = cursor.fetchone()
        connection.commit()

        if check_result:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            user_id = "_".join([f_name, l_name])
            query = "UPDATE employe SET first_name = %s, last_name = %s, user_id = %s, role = %s, salary_hourly = %s, email_id = %s, phone_number = %s, address = %s, postal_code = %s, updated_at = %s WHERE user_id = %s"
            value = (f_name, l_name, user_id, position, salary_hr, email, phone_number, address, postal, formatted_datetime, user_id)
            cursor.execute(query, value)
            connection.commit()
            
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
        


def addWholeDataApi():
    cursor = connection.cursor()
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO inventory (item_name, quantity_on_hand, unit, itme_price, category, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    vales = (
        ('guac', random.randint(0,7), 1, random.randint(40,500), 'food',formatted_datetime, formatted_datetime),
        ('green onions', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('cilantro', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('cheese', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('lettuce', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('cabbage', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('vellora', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('small white', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('big white', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('hige white', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('small whole', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('big whole', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('huge whole', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('sour cream', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('burrito sauce', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('hot sauce', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('taco', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('green ppr', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('tex max', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('ground beef', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('chicken brst', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('pulled beef', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('breaded cicken', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('pork', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('garlic', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('noodles', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('tomato', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('jalapinos', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('fries', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('chips', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('sweet potato', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('fish', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('shrimp', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('cheese cake', random.randint(0,7), 1, random.randint(40,500), 'food', formatted_datetime, formatted_datetime),
        ('pepsi bottle', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('pepsi can', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('diet pepsi bottle', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('diet pepsi can', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('pepsi zero', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito lime', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito mandarian', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito guava', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito mango', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito pineple', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito strawbery', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito fruit punch', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('jarrito maxican cola', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('crush', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('dr.ppr', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('mug of root bear', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('mountain due', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('7up bottel', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('7up can', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('aquafina', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('bubly lime', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('bubly blueberry', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('pure leaf lime', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('pure leaf rasbery', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('chcocolate milk', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('brisk bottle', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('brisk can', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('canada dry bottle', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('red bull', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('red bull suger free', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
        ('canada dry can', random.randint(0,7), 1, random.randint(40,500), 'drink', formatted_datetime, formatted_datetime),
    )

    cursor.executemany(query, vales)
    connection.commit()
    cursor.close()
    
    return {
            'status': 'sucess',
            'message': 'Data added'
        }
