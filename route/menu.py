from flask import Blueprint,  jsonify
from controller.menu import inventoryData, addWholeData

menu_blueprint = Blueprint('menu', __name__)
@menu_blueprint.route('/menu', methods=['GET'])
def inventory_data_api():
    page = inventoryData()
    return page

@menu_blueprint.route('/menu/item', methods=['PUSH'])
def add_whole_data_api():
    page = addWholeData()
    return page