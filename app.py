from flask import Flask
from flask_rest_jsonapi import Api
from shared.models import db
from resources.person import PersonList, PersonDetail

# Create the Flask application and the Flask-SQLAlchemy object.
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'

# Create the API object
api = Api(app)
api.route(PersonList, 'person_list', '/persons')
api.route(PersonDetail, 'person_detail', '/persons/<int:id>')

db.init_app(app)

# Start the flask loop
if __name__ == '__main__':
    app.run()
