#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import render_template

import sqlite3

app = Flask(__name__)

words = [
    {
        'id': 1,
        'title': u'asshole'
    },
    {
        'id': 2,
        'title': u'blowjob'
    }
]

con = sqlite3.connect('test.db')


#############
@app.route('/index')
def index():
    return render_template('index.html')

#############

@app.route('/curse/api/v1.0/words/', methods=['GET'])
def get_words():
    cur = con.cursor()
    cur.execute("select * from words")

    words = cur.fetchall();
    print "hello"
    return jsonify({'words':words})


@app.route('/curse/api/v1.0/words/<int:word_id>', methods=['GET'])
def get_word(word_id):
    word = [word for word in words if word['id'] == word_id]
    if len(word) == 0:
        abort(404)
    return jsonify({'word': word[0]})


@app.route('/curse/api/v1.0/words/', methods=['POST'])
def create_word():
    if not request.json or not 'title' in request.json:
        abort(400)
    word = {
        'id': words[-1]['id'] + 1,
        'title': request.json['title']
    }
    words.append(word)
    return jsonify({'word': word}), 201


@app.route('/curse/api/v1.0/words/<int:word_id>', methods=['PUT'])
def update_word(word_id):
    word = [word for word in words if word['id'] == word_id]
    if len(word) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    word[0]['title'] = request.json.get('title', word[0]['title'])

    return jsonify({'word': word[0]})


@app.route('/curse/api/v1.0/words/<int:word_id>', methods=['DELETE'])
def delete_word(word_id):
    word = [word for word in words if word['id'] == word_id]
    if len(word) == 0:
        abort(404)
    words.remove(word[0])
    return jsonify({'result': True})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
