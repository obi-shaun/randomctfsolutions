from flask import Flask
from pyngrok import ngrok
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello():
        return "<h1>Nothing to see here...>.></h1>"

if __name__ == "__main__":
        print(ngrok.connect(5000))
        app.run()
