import os
from dotenv import load_dotenv

load_dotenv()


class Config:
	"""For declaring the env variables"""
	SECRET_KEY = os.environ.get("SECRET_KEY")
	SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get("EMAIL_USER")
	MAIL_PASSWORD = os.environ.get("EMAIL_PASS")
	publishable_key = os.environ.get("STRIPE_PUBLISHABLE_KEY")
	secret_key = os.environ.get("STRIPE_SECRET_KEY")


