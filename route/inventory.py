from flask import Blueprint,  jsonify
from controller.inventory import inventoryData

inventory_blueprint = Blueprint('inventory', __name__)
@inventory_blueprint.route('/inventory', methods=['GET'])
def inventory_data_api():
    page = inventoryData()
    return page