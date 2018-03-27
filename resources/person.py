from flask_rest_jsonapi import ResourceDetail, ResourceList, \
    ResourceRelationship
from models.person import Person
from models.computer import Computer
from schemas.person import PersonSchema
from shared.models import db
from flask_rest_jsonapi.exceptions import ObjectNotFound
from sqlalchemy.orm.exc import NoResultFound


class PersonList(ResourceList):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}


class PersonDetail(ResourceDetail):
    def before_get_object(self, view_kwargs):
        if view_kwargs.get('computer_id') is not None:
            try:
                computer = self.session.query(Computer) \
                    .filter_by(id=view_kwargs['computer_id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'computer_id'},
                                     "Computer: {} not found"
                                     .format(view_kwargs['computer_id']))
            else:
                if computer.person is not None:
                    view_kwargs['id'] = computer.person.id
                else:
                    view_kwargs['id'] = None

    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person,
                  'methods': {'before_get_object': before_get_object}}


class PersonRelationship(ResourceRelationship):
    schema = PersonSchema
    data_layer = {'session': db.session,
                  'model': Person}
