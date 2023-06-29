import os

from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Database
    ALCHEMICAL_DATABASE_URL = os.environ.get(
        'ALCHEMICAL_DATABASE_URL'
    ) or 'sqlite:///' + os.path.join(basedir, 'db.db')
    ALCHEMICAL_ENGINE_OPTIONS = (
        os.environ.get('ALCHEMICAL_ENGINE_OPTIONS') or True
    )

    # API documentation
    APIFAIRY_TITLE = 'Simple CURD'
    APIFAIRY_VERSION = '1.0'
    APIFAIRY_UI = os.environ.get('APIFAIRY_DOCS_UI', 'swagger_ui')

    # Cors
    FLASK_CORS = os.environ.get('FLASK_CORS') or False

    # Server
    FLASK_ENV = os.environ.get('FLASK_ENV')
