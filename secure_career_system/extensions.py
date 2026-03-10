from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

try:
	from flask_login import LoginManager
except Exception:
	# minimal fallback when flask_login is not installed in the environment
	class LoginManager:
		def init_app(self, app):
			return None

		def user_loader(self, fn):
			return fn

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
