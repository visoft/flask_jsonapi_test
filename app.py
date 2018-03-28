from flask import Flask
from flask_rest_jsonapi import Api
from flask_migrate import Migrate
from shared.models import db
from resources.person import PersonList, PersonDetail, PersonRelationship
from resources.computer import ComputerList, ComputerDetail, \
                               ComputerRelationship

# Create the Flask application and the Flask-SQLAlchemy object.
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'

with app.app_context():
    db.init_app(app)
    Migrate(app, db)

# Create the API object
api = Api(app)
api.route(PersonList, 'person_list', '/persons')
api.route(PersonDetail, 'person_detail', '/persons/<int:id>',
          '/computers/<int:computer_id>/owner')
api.route(PersonRelationship, 'person_computers',
          '/persons/<int:id>/relationships/computers')
api.route(ComputerList, 'computer_list', '/computers',
          '/persons/<int:id>/computers')
api.route(ComputerDetail, 'computer_detail', '/computers/<int:id>')
api.route(ComputerRelationship, 'computer_person',
          '/computers/<int:id>/relationships/owner')


# Start the flask loop
if __name__ == '__main__':
    app.run()
