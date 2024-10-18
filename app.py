from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Function to connect to the SQLite database
def connect_db():
    conn = sqlite3.connect('test.db')
    conn.row_factory = sqlite3.Row  # This allows us to return rows as dictionaries
    return conn

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = connect_db()
    cursor = conn.cursor()

    # Query to select all users from the database
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    # Convert the query result into a list of dictionaries
    users_list = []
    for user in users:
        users_list.append({
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'age': user['age']
        })

    conn.close()
    return jsonify(users_list)

# Route to get a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Query to select a user by ID
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({
            'id': user['id'],
            'name': user['name'],
            'email': user['email'],
            'age': user['age']
        })
    else:
        return jsonify({'error': 'User not found'}), 404

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    conn = connect_db()
    cursor = conn.cursor()

    # Get the data from the request
    new_user = request.get_json()

    name = new_user.get('name')
    email = new_user.get('email')
    age = new_user.get('age')

    if not name or not email or not age:
        return jsonify({'error': 'Name, email, and age are required'}), 400

    # Insert the new user into the database
    cursor.execute('''
        INSERT INTO users (name, email, age) 
        VALUES (?, ?, ?)
    ''', (name, email, age))

    conn.commit()

    # Get the last inserted ID
    user_id = cursor.lastrowid

    conn.close()

    # Return the created user as a response
    return jsonify({
        'id': user_id,
        'name': name,
        'email': email,
        'age': age
    }), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)