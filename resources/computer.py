from flask_rest_jsonapi import ResourceDetail, ResourceList, \
    ResourceRelationship
from models.person import Person
from models.computer import Computer
from schemas.computer import ComputerSchema
from shared.models import db
from flask_rest_jsonapi.exceptions import ObjectNotFound
from sqlalchemy.orm.exc import NoResultFound


class ComputerList(ResourceList):
    def query(self, view_kwargs):
        query_ = self.session.query(Computer)
        if view_kwargs.get('id') is not None:
            try:
                self.session.query(Person).filter_by(
                                            id=view_kwargs['id']).one()
            except NoResultFound:
                raise ObjectNotFound({'parameter': 'id'}, "Person: {} not \
                                     found".format(view_kwargs['id']))
            else:
                query_ = query_.join(Person).filter(
                                        Person.id == view_kwargs['id'])
        return query_

    def before_create_object(self, data, view_kwargs):
        if view_kwargs.get('id') is not None:
            person = self.session.query(Person).filter_by(
                                                id=view_kwargs['id']).one()
            data['person_id'] = person.id

    schema = ComputerSchema
    data_layer = {'session': db.session,
                  'model': Computer,
                  'methods': {'query': query,
                              'before_create_object': before_create_object}}


class ComputerDetail(ResourceDetail):
    schema = ComputerSchema
    data_layer = {'session': db.session,
                  'model': Computer}


class ComputerRelationship(ResourceRelationship):
    schema = ComputerSchema
    data_layer = {'session': db.session,
                  'model': Computer}
