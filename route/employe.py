from flask import Blueprint,  jsonify
from controller.employe import employeData, addEmployeData

employe_blueprint = Blueprint('employe', __name__)
@employe_blueprint.route('/employe', methods=['GET'])
def employe_data_api():
    data = employeData()
    return data

@employe_blueprint.route('/employe/add', methods=['PUSH'])
def employe_data_api():
    data = employeData()
    return data