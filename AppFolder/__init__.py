from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import click
import os


#Init app

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFCATIONS']= False

#init db

db= SQLAlchemy(app)

#Init Marshmallow

ma = Marshmallow(app)

from AppFolder.Routes import UsersRoutes	
from AppFolder.Routes.Results import ResultsAARRoutes
from AppFolder.Routes.Results import ResultsOccupancyRoutes
from AppFolder.Routes.Results import LocalityAgentRoutes
from AppFolder.Routes.Results import LocalityRentRoutes
from AppFolder.Routes.Results import AgentRoutes

#in anaconda set FLASK_APP=run.py then run the commmand

from AppFolder.script1 import reset_db,setupAirDna,setupRPD

@app.cli.command("initdb")
def initdb_command():
	reset_db()

@app.cli.command("setupAirDna")
def setupAirDna_command():
	setupAirDna()

@app.cli.command("setupRPD")
def setupRPD_command():
	setupRPD()