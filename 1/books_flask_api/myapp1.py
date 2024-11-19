from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

books_list = [
    {
        "id": 1,
        "title":"Eloquent JavaScript, Third Edition",
        "author":"Marijn Haverbeke",
        "publisher":"No Starch Press",
    },
    {
        "id": 2,
        "title":"Practical Modern JavaScript",
        "author":"Nicolás Bevacqua",
        "publisher":"O'Reilly Media",
    },
    {
        "id": 3,
        "title":"Understanding ECMAScript 6",
        "author":"Nicholas C. Zakas",
        "publisher":"No Starch Press",
    },
    {
        "id": 4,
        "title":"Speaking JavaScript",
        "author":"Axel Rauschmayer",
        "publisher":"O'Reilly Media",
    },
    {
        "id": 5,
        "title":"Learning JavaScript Design Patterns",
        "author":"Addy Osmani",
        "publisher":"O'Reilly Media",
    },
    {
        "id": 6,
        "title":"You Don't Know JS Yet",
        "author":"Kyle Simpson",
        "publisher":"Independently published"
    },
    {
        "id": 7,
        "title":"Pro Git",
        "author":"Scott Chacon and Ben Straub",
        "publisher":"Apress; 2nd edition",
    },
    {
        "id": 8,
        "title":"Rethinking Productivity in Software Engineering",
        "author":"Caitlin Sadowski, Thomas Zimmermann",
        "publisher":"Apress",
    },
]


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/<name>')
def print_name(name):
    return f"<p>Hi {name}, welcome to custom page...<p>"

@app.route("/books", methods=['GET', 'POST'])
def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)
        else:
            return 'Nothing Found', 404
    
    if request.method == 'POST':
        new_title = request.form['title']
        new_author = request.form['author']
        new_publisher = request.form['publisher']
        iD = books_list[-1]['id']+1

        new_obj = {
            'title': new_title,
            'author': new_author,
            'publisher': new_publisher,
            'id': iD
        }

        books_list.append(new_obj)
        return jsonify(books_list), 201
    
@app.route('/book/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_book(id):
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            pass
    
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['author'] = request.form['author']
                book['title'] = request.form['title']
                book['publisher'] = request.form['publisher']

                updated_obj = {
                    'id': id,
                    'title': book['title'],
                    'author': book['author'],
                    'publisher': book['publisher']
                }

                return jsonify(updated_obj)
            
    
        



