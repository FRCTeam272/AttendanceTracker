from flask import Flask, request, jsonify
from server_functions import sf
app = Flask("attendance_tracker")

@app.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    student_name = data.get('name')
    student_id = data.get('id')
    
    if not student_name or not student_id:
        return jsonify({"error": "Invalid input"}), 400
    
    try:
        sf.add_student(student_id, student_name)
        return jsonify({"message": "Student added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

