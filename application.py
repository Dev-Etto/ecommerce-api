from typing import List
from flask import Flask, jsonify, request
from flask_login import UserMixin, current_user, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


application = Flask(__name__)
application.config['SECRET_KEY'] = 'minhas_chave_123'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

login_maneger = LoginManager()
database = SQLAlchemy(application)
login_maneger.init_app(application)
login_maneger.login_view = 'login'
CORS(application)

class Product(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(120), nullable=False)
    price = database.Column(database.Float, nullable=False)
    description = database.Column(database.Text, nullable=True)

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), nullable=False, unique=True)
    password = database.Column(database.String(80), nullable=True)
    cart = database.relationship('CartItem', backref='user', lazy=True)

class CartItem(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id =  database.Column(database.Integer, database.ForeignKey('user.id'), nullable=False)
    product_id = database.Column(database.Integer, database.ForeignKey('product.id'), nullable=False)


## Authentication

@login_maneger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@application.route('/login', methods=['POST'])
def login():
    data = request.json

    if not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required'}), 400

    user: User = User.query.filter_by(username=data.get('username')).first()

    if user and data.get('password') == user.password:
        login_user(user)
        return jsonify({'message': 'Logged in successfully'}), 200

    return jsonify({'message': 'Unauthorized. Invalid credentials'}), 401


@application.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})


## Products

@application.route('/api/products/add', methods=['POST'])
@login_required
def add_product():
    data = request.json

    if 'name' in data and 'price' in data:

        product = Product(name=data['name'], price=data['price'], description=data.get('description', ''))

        database.session.add(product)

        database.session.commit()

        return jsonify({'message':'Product add successfully'}), 200

    return jsonify({'message':"Invalid product data"}), 400

@application.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
@login_required
def delete_product(product_id):
    product = Product.query.get(product_id)

    if product:
        database.session.delete(product)
        database.session.commit()
        return jsonify({'message':'Product add successfully'}), 200

    return jsonify({'message':"Invalid product data"}), 404


@application.route('/api/products/<int:product_id>', methods=['GET'])
@login_required
def get_product_detail(product_id):
    product = Product.query.get(product_id)

    if product:
        return jsonify({
            'id':product.id,
            'name':product.name,
            'price':product.price,
            'description':product.description
        }), 200

    return jsonify({"message":"Product not found"}), 404

@application.route('/api/products/update/<int:product_id>', methods=['PUT'])
@login_required
def update_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({'message':'Project not found'}), 404
    
    data = request.json

    if 'name' in data:
        product.name = data['name']
    
    if 'price' in data:
        product.price = data['price']

    if 'description' in data:
        product.description = data['description']

    database.session.commit()

    return jsonify({'message':'Product updated successfully'}), 200

@application.route('/api/products', methods=['GET'])
def get_products():
    products :List[Product]= Product.query.all()

    print(f"Usuário autenticado: {current_user.is_authenticated}")
    
    product_list = []

    for product  in products:
        product_data = {
            'id':product.id,
            'name':product.name,
            'price':product.price,
        }
        product_list.append(product_data)

    return jsonify(product_list), 200


# Checkout

@application.route('/api/cart/add/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):

    user = User.query.get(int(current_user.id))

    product =  Product.query.get(int(product_id))

    if user and product:
        cart_item = CartItem(user_id=user.id, product_id=product.id)

        database.session.add(cart_item)
        database.session.commit()

        return jsonify({'message':'Item added to the cart Successfully'}), 200

    return jsonify({'message':'Failed to add item to the cart'}), 400

@application.route('/api/cart/remove/<int:product_id>', methods=['DELETE'])
@login_required
def remove_from_cart(product_id):
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=Product.id).first()
    if cart_item:
        database.session.delete(cart_item)
        database.session.commit()

        return jsonify({'message':'Item removed from the cart successfully'}), 200
    
    return jsonify({'message':'Failed to remove item from the cart'}), 400

@application.route('/api/cart', methods=['GET'])
@login_required
def view_cart():
    user = User.query.get(int(current_user.id))

    cart_items = user.cart
    cart_content = []

    for cart_item in cart_items:
        product = Product.query.get(cart_item.product_id)
        cart_content.append(
                {
                    'id': cart_item.id,
                    'user_id': cart_item.user_id,
                    'product_id': cart_item.product_id,
                    'product_name': product.name,
                    'product_price': product.price
                    }
                )
    
    return jsonify(cart_content), 200

@application.route('/api/cart/checkout', methods=['POST'])
@login_required
def checkout():
    user = User.query.get(current_user.id)

    cart_items = user.cart

    for cart_item in cart_items:
        database.session.delete(cart_item)

    database.session.commit()

    return jsonify({'message':'Checkout sucessfully. Cart  ha been cheared'}), 200


if __name__ == "__main__":
    application.run(debug=True)
