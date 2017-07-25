from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'ajaxnotes')
app.secret_key = 'some_secret'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getnotes')
def notes():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)
    return render_template('partials/notes.html', all_notes=notes)

@app.route('/notes/create', methods = ['POST'])
def create():
    query = "INSERT INTO notes(title, created_at, updated_at) VALUES('{}', NOW(), NOW())".format(request.form['title'])
    mysql.query_db(query)
    return redirect('/getnotes')

@app.route('/notes/<id>/destroy', methods=["POST"])
def delete(id):
    query = "DELETE FROM notes WHERE id = :id"
    data = { 'id': id}
    mysql.query_db(query, data)
    return redirect('/getnotes')

@app.route('/notes/<id>/update', methods=["POST"])
def update(id):
    query = "UPDATE notes SET description = :description, updated_at = NOW() WHERE id = :id"
    data = { 'description': request.form['description'], 'id': id}
    mysql.query_db(query, data)
    return redirect('/getnotes')

app.run(debug=True)
