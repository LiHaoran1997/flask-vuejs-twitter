import os

import flask

from app import create_app
app = create_app()

print(os.path.dirname(app.instance_path))