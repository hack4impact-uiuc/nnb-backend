from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import db
import api

manager = Manager(api)
migrate = Migrate(api, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
