# impoerting flask libraries for server
import flask 
from route.employe import employe_blueprint
from route.inventory import inventory_blueprint

app = flask.Flask(__name__)
app. register_blueprint(employe_blueprint, url_prefix='/api')
app. register_blueprint(inventory_blueprint, url_prefix='/api')

# Start server
if (__name__ == "__main__"):
    app.run(debug=True)
