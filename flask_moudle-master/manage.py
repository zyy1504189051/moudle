#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_script import Manager, Server
from app import app, api
from app.urls import urls

manager = Manager(app)
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',
    port=5000)
)

if __name__ == "__main__":
    for url in urls:
        api.add_resource(*url)
    manager.run()
