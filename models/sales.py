from flask import Flask, render_template, jsonify, request
from db_connection import config, connection, cursor
import datetime
import json
import random

# Simulated async function
def getSaleDataApi():
    cursor = connection.cursor()
    query = "SELECT sale_date, SUM(total_price) as total_sale FROM sales GROUP BY sale_date ORDER BY sale_date"
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()

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

    start_date = datetime.date(2023, 2, 1)
    end_date = datetime.date(2025, 1, 2)

    # set store hours
    store_open = datetime.time(11, 0)
    store_close = datetime.time(0, 0)

    # set 15 minutes interval
    interval = datetime.timedelta(minutes=15)

    current_date = start_date

    # build while loop for days
    data = []
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
            item = item_id[random.randint(0,51)][0]
            qun = random.randint(1, 10)
            item_price = cursor.execute("SELECT sale_price FROM menu_item WHERE item_id = %s", [item])
            item_price = cursor.fetchone()
            connection.commit()
            
            price = qun * item_price[0]
            x = [
                date,
                time,
                day,
                item,
                qun,
                price,
                1
            ]
            data.append(x)
            dt_start = dt_next

    query = "INSERT INTO sales (sale_date, sale_time, sale_day, item_id, quantity, total_price, store_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(query, data)
    connection.commit()
    cursor.close()
    return {
            'status': 'sucess',
            'message': 'Data added'
        }
