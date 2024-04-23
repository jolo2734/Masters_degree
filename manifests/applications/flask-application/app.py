import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Environment variables for Elasticsearch
es_host = os.getenv('ELASTICSEARCH_HOST', 'elasticsearch')
es_port = os.getenv('ELASTICSEARCH_PORT', '9200')
es_password = os.getenv('ELASTICSEARCH_PASSWORD', 'example')

# Environment variables for PostgreSQL
pg_user = os.getenv('POSTGRES_USER', 'user')
pg_password = os.getenv('POSTGRES_PASSWORD', 'password')
pg_db = os.getenv('POSTGRES_DB', 'mydatabase')
pg_host = os.getenv('POSTGRES_HOST', 'postgres')
pg_port = os.getenv('POSTGRES_PORT', '5432')

# Configure SQLAlchemy for PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure Elasticsearch client
es = Elasticsearch([{'host': es_host, 'port': es_port}], http_auth=('elastic', es_password))

class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Record {self.name}>'

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Flask App</title>
        </head>
        <body>
            <h1>Simple Flask App UI</h1>
            <form action="/add" method="post">
                <input type="text" name="name" placeholder="Enter name" required>
                <input type="text" name="description" placeholder="Enter description" required>
                <button type="submit">Add Record</button>
            </form>
            <p>Use the API endpoint /search?query=text_to_search to search records.</p>
        </body>
    </html>
    '''

@app.route('/add', methods=['POST'])
def add_data():
    name = request.json['name']
    description = request.json['description']
    record = Record(name=name, description=description)
    db.session.add(record)
    db.session.commit()
    es.index(index='records', doc_type='record', id=record.id, body={'name': name, 'description': description})
    return jsonify({'id': record.id, 'name': name, 'description': description}), 201

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    res = es.search(index="records", body={"query": {"match": {"description": query}}})
    return jsonify([hit['_source'] for hit in res['hits']['hits']]), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
