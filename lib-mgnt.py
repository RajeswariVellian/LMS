import sqlite3
from datetime import date
from flask import Flask, request, redirect, render_template, url_for, jsonify

app = Flask(__name__, template_folder='template')


@app.route('/', methods=['GET'])
def main_menu():
    return render_template('main_menu.html')


@app.route('/list_books', methods=['POST'])
def get_books():
    conn = sqlite3.connect("C:\Raji\PythonPrograms\sqlite-tools-win32-x86-3320300\library.db")
    search_record = """select * from book_master;"""
    cursor = conn.execute(search_record)
    rec_list = []
    for val in cursor:
        rec_list.append(val)
    return render_template('list_books.html', list1=rec_list)


@app.route('/add_menu')
def add_menu():
    return render_template('add_books.html')


@app.route('/add_books', methods=['GET', 'POST'])
def add_book():
    conn = sqlite3.connect("C:\Raji\PythonPrograms\sqlite-tools-win32-x86-3320300\library.db")
    insert_record_template = """insert into book_master values("{}","{}","{}","{}","{}","{}","{}","{}","{}");"""
    book_id = request.form['book_id']
    name = request.form['name']
    author = request.form['author']
    publications = request.form['publications']
    flag = request.form['flag']
    created_by = request.form['created_by']
    created_date = request.form['created_date']
    modified_by = request.form['modified_by']
    modified_date = request.form['modified_date']
    insert_record = insert_record_template.format(book_id, name, author, publications, flag, created_by, created_date, modified_by, modified_date)
    conn.execute(insert_record)
    conn.commit()
    return render_template('add_books.html')


if __name__ == '__main__':
    app.run()
