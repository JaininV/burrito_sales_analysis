#Import users function from model folder
from flask import Flask, render_template, jsonify, request
from models.menu import getMenuDataApi, addWholeDataApi
import asyncio

def menuData():
    page = getMenuDataApi()
    return page

def addWholeData():
    page = addWholeDataApi()
    return page