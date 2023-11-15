import os

import dotenv

dotenv.load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
CELERY_BROKER = os.getenv("CELERY_BROKER")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Config(object):
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY = {
        "CELERY_BROKER_URL": CELERY_BROKER,
        "CELERY_RESULT_BACKEND": CELERY_RESULT_BACKEND,
        "CELERY_TASK_IGNORE_RESULT": True,
    }
