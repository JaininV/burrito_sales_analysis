from flask import Blueprint,  jsonify
from controller.sales import saleData, addSalesData

sales_blueprint = Blueprint('sales', __name__)
@sales_blueprint.route('/sales', methods=['GET'])
def sale_data_api():
    page = saleData()
    return page

@sales_blueprint.route('/sales/item', methods=['POST'])
def add_sales_data_api():
    page = addSalesData()
    return page