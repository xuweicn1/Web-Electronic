from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)
# app.debug = True
#
from app import routes
