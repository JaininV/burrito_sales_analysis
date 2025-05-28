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
    connection.close()

    return {
        'data': result
    }

def addSalesDataApi():
    cursor = connection.cursor()
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    
    item_id = "SELECT item_id FROM menu_item WHERE active = %s"
    cursor.execute(item_id, [1])
    item_id = cursor.fetchall()
    connection.commit()

    
    return {
            'status': 'sucess',
            'message': 'Data added'
        }
