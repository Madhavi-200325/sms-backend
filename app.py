from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database Connection
conn = mysql.connector.connect(
    host="dpg-cvldve56ubrc73bidcng-a",
    user="root",
    password="jrrSnnJLM80nBeqkUeZqKqnJQwmzu2Wh",
    database="student_management_c8hy"
)
cursor = conn.cursor(dictionary=True)

# Get all students
@app.route('/students', methods=['GET'])
def get_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return jsonify(students)

# Add student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    query = "INSERT INTO students (name, email, age, course) VALUES (%s, %s, %s, %s)"
    values = (data['name'], data['email'], data['age'], data['course'])
    cursor.execute(query, values)
    conn.commit()
    return jsonify({"message": "Student added successfully"}), 201

# Update student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    query = "UPDATE students SET name=%s, email=%s, age=%s, course=%s WHERE id=%s"
    values = (data['name'], data['email'], data['age'], data['course'], id)
    cursor.execute(query, values)
    conn.commit()
    return jsonify({"message": "Student updated successfully"})

# Delete student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (id,))
    conn.commit()
    return jsonify({"message": "Student deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
