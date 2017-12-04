from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from api import db, app, set_heroku_config
from api.models import PointsOfInterest, Maps, StoryNames, Stories, AdditionalLinks

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    app.run(debug=True)


@manager.command
def runworker():
    app.run()
    set_heroku_config()


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    manager.run()
