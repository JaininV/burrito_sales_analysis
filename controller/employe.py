#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.employe import getEmployeDataApi
import asyncio

def employeData():
    employe_data = getEmployeDataApi()
    return employe_data

