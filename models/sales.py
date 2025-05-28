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
    
    # item_id = "SELECT item_id FROM menu_item WHERE active = %s"
    # cursor.execute(item_id, [1])
    # item_id = cursor.fetchall()
    # connection.commit()

    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 1, 2)

    # set store hours
    store_open = datetime.time(11, 0)
    store_close = datetime.time(0, 0)

    # set 15 minutes interval
    interval = datetime.timedelta(minutes=15)

    current_date = start_date

    # build while loop for days
    while current_date < end_date:
        # start time
        dt_start = datetime.datetime.combine(current_date, store_open)

        # end time
        dt_end = dt_start.replace(hour = 23, minute=59)
        current_date += datetime.timedelta(days=1)

        while dt_start <= dt_end:
            dt_next = dt_start + interval
            date = dt_next.date()
            time = dt_next.time()
            day = dt_next.strftime("%A")
            
            dt_start = dt_next

    return {
            'status': 'sucess',
            'message': 'Data added'
        }
