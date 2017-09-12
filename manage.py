from flask_script import Manager, Server
from app import app

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000))