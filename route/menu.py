from flask import Blueprint,  jsonify
from controller.menu import menuData, addWholeData

menu_blueprint = Blueprint('menu', __name__)
@menu_blueprint.route('/menu', methods=['GET'])
def menu_data_api():
    page = menuData()
    return page

@menu_blueprint.route('/menu/item', methods=['POST'])
def add_whole_data_api():
    page = addWholeData()
    return page