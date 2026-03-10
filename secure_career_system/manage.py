from secure_career_system.app import app, db
from flask_migrate import Migrate, upgrade

migrate = Migrate(app, db)

def run_upgrade():
    with app.app_context():
        upgrade()

if __name__ == '__main__':
    app.run()
