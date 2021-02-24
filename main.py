from flask import Flask, redirect
from flask_restful import Api
# from resources.product import ItemList, Item
from resources.product import Item
from flask_jwt import JWT
from security import authentication, identity
from resources.user import RegisterUser


app = Flask(__name__)
app.secret_key = "my_secret_key"
app.config['PROPAGATE-EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

api = Api(app)
jwt = JWT(app, authentication, identity)


@app.route("/")
def home():
    return redirect("https://github.com/Maria-555/unilab_rest_api/tree/main"), 302


# api.add_resource(ItemList, "/items")
api.add_resource(Item, "/items/<string:name>")
api.add_resource(RegisterUser, "/registration")

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, port=5000)
