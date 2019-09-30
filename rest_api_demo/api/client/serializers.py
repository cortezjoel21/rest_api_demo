from flask_restplus import fields
from rest_api_demo.api.restplus import api

client_user = api.model('Client user', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a client user'),
    'name': fields.String(required=True, description='Client name'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_client_users = api.inherit('Page of client users', pagination, {
    'items': fields.List(fields.Nested(client_user))
})
