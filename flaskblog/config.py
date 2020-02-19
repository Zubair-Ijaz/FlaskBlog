import os


class Config:
	"""docstring for Config"""
	#SECRET_KEY = '1dbaea1b837840b8f53b662484a738b3'
	#SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
	MAIL_SERVER = 'smtp.gmail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	# The values of these variables are set in environment variable settings.
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')