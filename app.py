from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

# MongoDB connection
mongo_host = os.environ.get('MONGO_HOST', 'localhost')
client = MongoClient(f'mongodb://{mongo_host}:27017/')
db = client['student_db']
students = db['students']

@app.route('/')
def index():
    all_students = students.find()
    return render_template('index.html', students=all_students)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    roll = request.form['roll']
    dept = request.form['dept']
    students.insert_one({'name': name, 'roll': roll, 'dept': dept})
    return redirect('/')

@app.route('/delete/<id>', methods=['POST'])
def delete_student(id):
    students.delete_one({'_id': ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
