from flask import Flask, Blueprint
from routes.main import main

app = Flask(__name__)

app.register_blueprint(main)

app.run(
    debug=True
)