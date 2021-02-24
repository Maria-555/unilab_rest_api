from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.product import ItemModels


# class ItemList(Resource):
#     # TABLE_NAME = 'places'
#
#     def get(self):
#         return self.query.all()
#
#     def delete(self):
#         pass


class Item(Resource):
    # TABLE_NAME = 'places'

    my_parser = reqparse.RequestParser()
    my_parser.add_argument('name',
                           type=str,
                           required=True,
                           help="New object must contain argument - 'name' and it must be a string format")
    my_parser.add_argument('status',
                           type=str,
                           required=True,
                           help="New object must contain argument - 'status' and it must be a string format")

    def get(self, name):
        item = ItemModels.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Place not found"}, 404

    @jwt_required()
    def post(self, name):
        data = Item.my_parser.parse_args()

        if ItemModels.find_by_name(name):
            return {"message": "Place with this name already exists"}, 400

        item = ItemModels(data['name'], data['status'])

        try:
            item.add_item_to_db()

        except:
            return {"message": "Error while inserting a place."}

        return item.json(), 201

    @jwt_required()
    def put(self, name):
        data = Item.my_parser.parse_args()
        item = ItemModels.find_by_name(name)

        if item:
            item.status = data['status']

        else:
            item = ItemModels(data['name'], data['status'])

        item.add_item_to_db()

        return item.json()

    @jwt_required()
    def delete(self, name):
        item = ItemModels.find_by_name(name)

        if item:
            item.delete_item_from_db()
            return {"message": "Place was successfully deleted"}, 200

        return {"message": "Place with this name was not found"}, 404
