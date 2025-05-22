#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.employe import getEmployeDataApi, addEmployeDataApi
import asyncio

def employeData():
    data = getEmployeDataApi()
    return data

def addEmployeData():
    data = addEmployeDataApi(data)
    return data