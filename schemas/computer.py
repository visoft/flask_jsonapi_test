from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class ComputerSchema(Schema):
    class Meta:
        type_ = 'computer'
        self_view = 'computer_detail'
        self_view_kwargs = {'id': '<id>'}

    id = fields.Integer(as_string=True, dump_only=True)
    serial = fields.Str(requried=True)
    name = fields.Str(requried=True)
    owner = Relationship(attribute='person',
                         self_view='computer_person',
                         self_view_kwargs={'id': '<id>'},
                         related_view='person_detail',
                         related_view_kwargs={'computer_id': '<id>'},
                         schema='PersonSchema',
                         type_='person')
