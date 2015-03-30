from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ASECRETKEY'

client = MongoClient('localhost', 27017)
db = client.rabit

import rabit.views
