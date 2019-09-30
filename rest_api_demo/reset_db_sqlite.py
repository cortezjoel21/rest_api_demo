from rest_api_demo.app import initialize_app, app
from rest_api_demo.database import reset_database

initialize_app(app)
with app.app_context():
    reset_database()