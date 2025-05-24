#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.employe import getEmployeDataApi, addEmployeDataApi, upadteEmployeDataApi
import asyncio

def employeData():
    data = getEmployeDataApi()
    return data

def addEmployeData():
    data = request.form
    page = addEmployeDataApi(data)
    return page

def updateEmployeData():
    data = request.form
    page = upadteEmployeDataApi(data)
    return page