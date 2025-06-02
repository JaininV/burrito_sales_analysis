from flask import Flask, render_template, jsonify, request
from db_connection import connection, cursor
import datetime
import json
import random

# Simulated async function
def getMenuDataApi():
    query = "SELECT * FROM inventory"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    

    return {
        'data': result
    }

def addWholeDataApi():
    cursor = connection.cursor()
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    query = "INSERT INTO menu_item (name, description, category, cost_price, sale_price, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    vales = (
        ('small veggie burrito', 'small veggie burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small tofu burrito', 'small tofu burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small sweet potato burrito', 'small sweet potato burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small rosted chicken burrito', 'small rosted chicken burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small breaded chicken burrito', 'small breaded chicken burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small ground beef burrito', 'small ground beef burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small pulled beef burrito', 'small pulled beef burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small pork burrito', 'small pork burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small fish burrito', 'small fish burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small shrimp burrito', 'small shrimp burrito', 'small burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big veggie burrito', 'big veggie burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big tofu burrito', 'big tofu burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big sweet potato burrito', 'big sweet potato burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big rosted chicken burrito', 'big rosted chicken burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big breaded chicken burrito', 'big breaded chicken burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big ground beef burrito', 'big ground beef burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big pulled beef burrito', 'big pulled beef burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big pork burrito', 'big pork burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big fish burrito', 'big fish burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('big shrimp burrito', 'big shrimp burrito', 'big burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge veggie burrito', 'huge veggie burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge tofu burrito', 'huge tofu burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge sweet potato burrito', 'huge sweet potato burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge rosted chicken burrito', 'huge rosted chicken burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge breaded chicken burrito', 'huge breaded chicken burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge ground beef burrito', 'huge ground beef burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge pulled beef burrito', 'huge pulled beef burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge pork burrito', 'huge pork burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge fish burrito', 'huge fish burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('huge shrimp burrito', 'huge shrimp burrito', 'huge burrito', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl veggie', 'bowl veggie', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl tofu', 'bowl tofu', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl sweet potato', 'bowl sweet potato', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl rosted chicken', 'bowl rosted chicken', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl breaded chicken', 'bowl breaded chicken', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl ground beef', 'bowl ground beef', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl pulled beef', 'bowl pulled beef', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl pork', 'bowl pork', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl fish', 'bowl fish', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('bowl shrimp', 'bowl shrimp', 'bowl', random.randint(10,12), random.randint(12,17), formatted_datetime, formatted_datetime),
        ('small fries', 'small fries', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('large fries', 'large fries', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('chips and salsa', 'chips and salsa', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('chips and guac', 'chips and guac', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('chips and queso', 'chips and queso', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('chicken empanada', 'chicken empanada', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('ground beef empanada', 'small fries', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('mars bar', 'mars bar', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('cheesecake burrito', 'cheese cake burrito', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('churros', 'churros', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('loaded fries', 'loaded fries', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
        ('loaded nachos', 'loaded nachos', 'side', random.randint(7,8), random.randint(8,11), formatted_datetime, formatted_datetime),
    )

    cursor.executemany(query, vales)
    connection.commit()
    cursor.close()
    
    return {
            'status': 'sucess',
            'message': 'Data added'
        }
