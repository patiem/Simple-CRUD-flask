# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and
# will be disabled by default in the future
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = "sqlite:///" + BASE_DIR + '/db.db'
