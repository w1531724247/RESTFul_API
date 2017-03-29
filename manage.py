from app import create_app, db
from app.models import User
from flask_migrate import Migrate, MigrateCommand, upgrade
from flask_script import Manager, Shell

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

