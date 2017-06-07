#!/usr/bin/env python
import os
from app import creat_app, db
from app.models import User
from flask_script import Manager, Shell

app = creat_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

def make_shell_context():
    return dict(app = app, db = db, User = User)
manager.add_command("shell", Shell(make_shell_context))

if __name__ == '__main__':
    manager.run()