# impoerting flask libraries for server
import flask 

app = flask.Flask(__name__)

# Start server
if (__name__ == "__main__"):
    app.run(debug=True)
