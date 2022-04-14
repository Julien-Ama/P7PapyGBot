from .parser import Parser
from .api_geo import GeoWrapper
from .api_wiki import WikiWrapper

from flask import Flask

app = Flask(__name__)
from app import views