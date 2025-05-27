#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.menu import getInventoryDataApi, addWholeDataApi
import asyncio

def inventoryData():
    page = getInventoryDataApi()
    return page

def addWholeData():
    page = addWholeDataApi()
    return page