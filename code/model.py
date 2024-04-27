from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    product_code = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())

    def __init__(self, product_name, product_code, product_description, product_price, product_quantity):
        self.name = product_name
        self.product_code = product_code
        self.description = product_description
        self.price = product_price
        self.quantity = product_quantity

    def to_json(self):
        return {
            'product_id': self.id,
            'product_name': self.name,
            'product_code': self.product_code,
            'product_description': self.description,
            'product_price': self.price,
            'quantity': self.product_quantity,
        }


class Order(db.Model):
    __tablename__ = 'Orders'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_ids = db.Column(db.JSON)
    order_quantity = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'product_ids': self.product_ids,
            'order_quantity': self.order_quantity,
            'order_price': self.order_price,
            'total_price': self.total_price,
        }

    def __init__(self, user_id, product_ids, order_quantity, order_price):
        self.user_id = user_id
        self.product_ids = product_ids
        self.order_quantity = order_quantity
        self.order_price = order_price
        self.total_price = order_price
