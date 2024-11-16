from flask import Flask, jsonify, request

app = Flask(__name__)

employee_list = [
    {
        'id': 1,
        'name': 'Junai',
        'occupation': 'IT Engineer'
    }
]

@app.route('/')
def index():
    return '<p>Hi, welcome to books api.</p>'

@app.route('/<name>')
def print_name(name):
    return f"<h3><p>Hello {name}</p><h3>"

@app.route('/employees', methods=['GET', 'POST'])
def employee():
    if request.method == 'GET':
        if len(employee_list) > 0:
            return jsonify(employee_list)
        else:
            return 'Not Found', 404
        
    if request.method == 'POST':
        iD = employee_list[-1]['id']
        new_name = request.form['name']
        new_occupation = request.form['occupation']
        
        new_object = {
            'id': iD,
            'name': new_name,
            'occupation': new_occupation
        }
        
        employee_list.append(new_object)
        return jsonify(employee_list), 201
        
        



