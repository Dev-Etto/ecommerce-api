# E-commerce API

This is a Flask-based API for an e-commerce system. It provides endpoints for user authentication, product management, and cart operations.

## Features

- **Authentication**: Login and logout functionality using `Flask-Login`.
- **Product Management**: Add, update, delete, and retrieve product details.
- **Cart Operations**: Add items to the cart, view cart contents, remove items, and checkout.

## Requirements

- Python 3.8 or higher
- SQLite (default database)

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd ecommerce-api-py
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Initialize the database:
   ```python
   from application import database
   database.create_all()
   ```

## Running the Application

1. Start the Flask server:

   ```bash
   python application.py
   ```

2. Access the API at `http://127.0.0.1:5000`.

## API Endpoints

### Authentication

- **POST /login**: Log in with username and password.
- **POST /logout**: Log out the current user.

### Products

- **GET /api/products**: Retrieve all products.
- **GET /api/products/{product_id}**: Retrieve details of a specific product.
- **POST /api/products/add**: Add a new product (requires login).
- **PUT /api/products/update/{product_id}**: Update a product (requires login).
- **DELETE /api/products/delete/{product_id}**: Delete a product (requires login).

### Cart

- **POST /api/cart/add/{product_id}**: Add a product to the cart (requires login).
- **DELETE /api/cart/remove/{product_id}**: Remove a product from the cart (requires login).
- **GET /api/cart**: View the cart contents (requires login).
- **POST /api/cart/checkout**: Checkout and clear the cart (requires login).

## Swagger Documentation

The API is documented using Swagger. Refer to the `swagger-doc.x-yaml` file for detailed API specifications.

## Notes

- Ensure the database is initialized before running the application.
- Use a tool like Postman or cURL to test the API endpoints.

## License

This project is licensed under the MIT License.
