import logging

from flask import request
from flask_restplus import Resource
from rest_api_demo.api.client.business import create_client_user, update_user, delete_user
from rest_api_demo.api.client.serializers import client_user, page_of_client_users
from rest_api_demo.api.client.parsers import pagination_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import User

log = logging.getLogger(__name__)

ns = api.namespace('client/users', description='Operations related to client users')

@ns.route('/')
class UsersCollection(Resource):

    #@api.expect(pagination_arguments)
    #@api.marshal_with(page_of_client_users)
    def get(self):
        user = User.all()
        return user

    @api.expect(client_user)
    def post(self):
        print("===============post")
        """
        Creates a new client user.
        """
        print("===============request.json" + str(request.json))
        create_client_user(request.json)
        return None, 201

@ns.route('/<int:id>')
@api.response(404, 'user not found.')
class userItem(Resource):

    @api.marshal_with(client_user)
    def get(self, id):
        """
        Returns a client user.
        """
        return User.query.filter(User.id == id).one()

    @api.expect(client_user)
    @api.response(204, 'user successfully updated.')
    def put(self, id):
        """
        Updates a client user.
        """
        data = request.json
        update_user(id, data)

        print("=======id: " + str(id))
        print("=======data: " + str(data))
        return None, 204

    @api.response(204, 'user successfully deleted.')
    def delete(self, id):
        """
        Deletes client user.
        """
        delete_user(id)
        return None, 204
