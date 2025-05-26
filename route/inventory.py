from flask import Blueprint,  jsonify
from controller.inventory import inventoryData, addWholeData

inventory_blueprint = Blueprint('inventory', __name__)
@inventory_blueprint.route('/inventory', methods=['GET'])
def inventory_data_api():
    page = inventoryData()
    return page

@inventory_blueprint.route('/inventory/item', methods=['GET'])
def add_whole_data_api():
    page = addWholeData()
    return page