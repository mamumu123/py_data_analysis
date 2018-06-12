from flask import Flask, render_template, request, url_for, jsonify, json
from flask_bootstrap import Bootstrap
import db

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    count_message = db.get_count_message()
    all_message = db.get_all_message()
    return render_template('index.html', count_message=count_message, all_message=all_message)


@app.route('/add_teach', methods=['POST'])
def add_teach():
    data = request.get_json()
    tex1 = data.get('tex1')
    tex2 = data.get('tex2')
    print(type, tex1, tex2)
    cID = int(tex2.split(' ')[0])
    pID = int(tex1.split(' ')[0])
    print(cID, pID)
    db.insert_teach(cID, pID)
    return "hello"


@app.route('/add_choice', methods=['POST'])
def add_choice():
    data = request.get_json()
    tex1 = data.get('tex1')
    tex2 = data.get('tex2')
    print(type, tex1, tex2)
    cID = int(tex2.split(' ')[0])
    pID = int(tex1.split(' ')[0])
    print(cID, pID)
    db.insert_choice(cID, pID)
    return "hello"


@app.route('/select_lesson', methods=['POST'])
def select_lesson():
    data = request.get_json()
    lesson = data.get('choice')
    lesson_id = int(lesson.split(' ')[0])
    # print(lesson_id)
    lesson_info = db.select_lesson(lesson_id)
    print(lesson_info)
    return json.dumps(lesson_info)


@app.route('/add_score', methods=['POST'])
def add_score():
    data = request.get_json()
    no = data.get('No')
    cID = data.get('cID')
    dataForm = data.get('dataForm')
    db.add_score(no, cID, dataForm)
    print(dataForm)
    print(no)
    return ('hello')


@app.route('/query_stu', methods=['POST'])
def query_stu():
    query = db.query_all_stu()
    print(query)
    return json.dumps(query)


@app.route('/query_tea', methods=['POST'])
def query_tea():
    query = db.query_all_tea()
    print(query)
    return json.dumps(query)


@app.route('/query_stuto', methods=['POST'])
def query_stuto():
    query = db.query_stuto()
    print(query)
    return json.dumps(query)


@app.route('/query_teato', methods=['POST'])
def query_teato():
    query = db.query_teato()
    print(query)
    return json.dumps(query)


@app.route('/query_name', methods=['POST'])
def query_name():
    data = request.get_json()
    name = str(data.get('name').strip())
    query = db.query_name(name)
    return json.dumps(query)


if __name__ == '__main__':
    app.run(debug=True)
