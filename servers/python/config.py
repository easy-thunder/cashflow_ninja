import os

from dotenv import load_dotenv
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
from sqlalchemy import MetaData

from flask_session import Session

# Load environment variables
load_dotenv()

# Flask app and configuration
app = Flask(__name__, static_folder="./static", static_url_path="/static")

# API keys and configurations
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("The OPENAI_API_KEY environment variable is not set.")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

# Flask app configurations
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "default_secret_key")
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_USE_SIGNER"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI", "sqlite:///app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

# Flask extensions
Session(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})
metadata = MetaData(
    naming_convention={
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    }
)
db = SQLAlchemy(metadata=metadata)
ma = Marshmallow(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Initialize marshmallow
ma.init_app(app)

# Initialize API
api = Api(app)

# Initialize database
db.init_app(app)

# OpenAI client
app.openai_client = openai_client

if __name__ == "__main__":
    app.run(port=5555, debug=True)
