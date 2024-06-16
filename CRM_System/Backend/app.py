# app.py

from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection configuration
conn = psycopg2.connect(
    dbname='crm_database',
    user='your_username',
    password='your_password',
    host='localhost'
)
conn.autocommit = True
cursor = conn.cursor()

# Routes

# Get all customers or add a new customer
@app.route('/customers', methods=['GET', 'POST'])
def customers():
    if request.method == 'GET':
        cursor.execute("SELECT * FROM customers;")
        customers = cursor.fetchall()
        return jsonify(customers)
    elif request.method == 'POST':
        data = request.get_json()
        name = data['name']
        email = data.get('email', None)
        phone = data.get('phone', None)

        cursor.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s) RETURNING id;",
                       (name, email, phone))
        customer_id = cursor.fetchone()[0]
        return jsonify({"message": "Customer created successfully", "customer_id": customer_id}), 201

# Log a new interaction for a customer
@app.route('/interactions', methods=['POST'])
def interactions():
    data = request.get_json()
    customer_id = data['customer_id']
    interaction_type = data['type']
    details = data['details']

    cursor.execute("INSERT INTO interactions (customer_id, type, details) VALUES (%s, %s, %s) RETURNING id;",
                   (customer_id, interaction_type, details))
    interaction_id = cursor.fetchone()[0]
    return jsonify({"message": "Interaction logged successfully", "interaction_id": interaction_id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
