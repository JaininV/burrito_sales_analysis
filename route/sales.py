from flask import Blueprint,  jsonify
from controller.sales import inventoryData, addSalesData

sales_blueprint = Blueprint('sales', __name__)
@sales_blueprint.route('/sales', methods=['GET'])
def inventory_data_api():
    page = inventoryData()
    return page

@sales_blueprint.route('/sales/item', methods=['POST'])
def add_whole_data_api():
    page = addSalesData()
    return page