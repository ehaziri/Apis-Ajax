from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'ajaxposts')
app.secret_key = 'some_secret'


@app.route('/')
def index():
    query = "SELECT description FROM posts"
    posts = mysql.query_db(query)
    return render_template('index.html', all_posts=posts)

@app.route('/posts/create', methods = ['POST'])
def create():
    query = "INSERT INTO posts(description, created_at, updated_at) VALUES('{}', NOW(), NOW())".format(request.form['description'])
    mysql.query_db(query)
    query = "SELECT description FROM posts"
    posts = mysql.query_db(query)
    return render_template('partials/posts.html', all_posts=posts)


app.run(debug=True)
