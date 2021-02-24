from flask_restful import Resource, reqparse
from models.user import UserModel


class RegisterUser(Resource):
    # TABLE_NAME = 'users'

    my_parser = reqparse.RequestParser()
    my_parser.add_argument('username',
                           type=str,
                           required=True,
                           help="Username must be indicated!")
    my_parser.add_argument('password',
                           type=str,
                           required=True,
                           help="Password must be indicated!")

    def post(self):
        params = RegisterUser.my_parser.parse_args()

        if UserModel.find_by_username(params['username']):
            return {"message": "User with this username already exists."}, 400

        user = UserModel(params['username'], params['password'])
        user.add_user_to_db()

        return {"message": "User was created successfully."}, 201
