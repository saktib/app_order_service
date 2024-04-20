from flask import Flask, jsonify, request
from model import db, Order, Product
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    db.init_app(app)
    db.create_all()

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    print(orders)
    return jsonify([order.to_json() for order in orders]), 200

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_by_id(order_id):
    order = Order.query.get(order_id)
    return jsonify(order.to_json()), 200

@app.route('/orders', methods=['POST'])
def add_order():
    user_id = request.json.get('user_id')
    product_id = request.json.get('product_id')
    order_quantity = request.json.get('order_quantity')

    if not all([user_id, product_id, order_quantity]):
        return jsonify({'error': 'Missing required fields'}), 400

    print(request.json)
    prod = db.session.query(Product).get(product_id)
    order_price = order_quantity * prod.product_price
    try:
        order = Order(user_id, product_id, order_quantity, order_price)
        db.session.add(order)
        db.session.commit()
        return jsonify({"order": " added succesfully"}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/orders/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify({'message': 'Order deleted successfully'})
    else:
        return jsonify({'error': 'Order not found'}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010, debug=True)
