from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), unique=True, nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)

class Order(db.Model):
    __tablename__ = 'order'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    order_quantity = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Float, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    def __init__(self, user_id, product_id, order_quantity, order_price):
        self.user_id = user_id
        self.product_id = product_id
        self.order_quantity = order_quantity
        self.order_price = order_price
        self.total_price = order_price  # Assuming no additional costs
