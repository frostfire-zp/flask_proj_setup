# app.py

from project import app

#! This line is important for db migration
from project.models.models import *

if __name__ == '__main__':
    app.run(debug=True)
