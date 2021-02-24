from db import db


class ItemModels(db.Model):
    __tablename__ = 'places'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    status = db.Column(db.String(50))

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def json(self):
        return {"name": self.name, "status": self.status}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def add_item_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_item_from_db(self):
        db.session.delete(self)
        db.session.commit()
