import os


from app import create_app, db
from app.models import Equipment, PurchaseOrder, PurchaseEquipment, Enterprise, init_db

from flask_script import Manager, Shell, prompt_bool, Server

app = create_app(os.getenv('FLASK_CONFIG') or 'development')
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!<h1>'

def make_shell_context():
    return dict(app=app, db=db)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host="0.0.0.0", port=9000))

@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to lose all your data"):
        db.drop_all()	

@manager.command
def initdb():
    init_db() 

@manager.command
def dropdb():
    db.drop_all()


if __name__ == '__main__':
    manager.run()
