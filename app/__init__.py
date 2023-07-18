from flask import Flask
from Config import Configs

app = Flask(__name__)
app.config.from_object(Configs)



from app import routes