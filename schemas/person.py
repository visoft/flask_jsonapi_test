from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class PersonSchema(Schema):
    class Meta:
        type_ = 'person'
        self_view = 'person_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'person_list'

    id = fields.Integer(as_string=True, dump_only=True)
    name = fields.Str()
    computers = Relationship(self_view='person_computers',
                             self_view_kwargs={'id': '<id>'},
                             related_view='computer_list',
                             related_view_kwargs={'id': '<id>'},
                             many=True,
                             schema='ComputerSchema',
                             type_='computer')
