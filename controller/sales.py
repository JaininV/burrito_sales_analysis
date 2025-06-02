#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.sales import getSaleDataApi, addSalesDataApi
import asyncio

def saleData():
    page = getSaleDataApi()
    return page

def addSalesData():
    page = addSalesDataApi()
    return page