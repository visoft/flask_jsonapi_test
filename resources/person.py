from flask_rest_jsonapi import ResourceDetail, ResourceList
from models.person import Person, db
from schemas.person import PersonSchema


class PersonList(ResourceList):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}


class PersonDetail(ResourceDetail):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}
