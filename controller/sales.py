#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.sales import getInventoryDataApi, addSalesDataApi
import asyncio

def inventoryData():
    page = getInventoryDataApi()
    return page

def addSalesData():
    page = addSalesDataApi()
    return page