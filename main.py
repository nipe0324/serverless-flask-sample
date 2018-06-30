import os
from flask import Flask, request, jsonify, abort
import boto3


app = Flask(__name__)


TODOS_TABLE = os.environ['TODOS_TABLE']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TODOS_TABLE)

def get_todo(id):
    res = table.get_item(Key={ 'id': id })
    if 'Item' not in res:
        abort(404)
    return res['Item']

def new_id():
    # bad implementation
    # maybe use numbering table or use uuid as id
    res = table.scan()
    ary = res['Items']
    if len(ary) == 0:
        return '1'
    else:
        ary = sorted(ary, key=lambda x: x['id'], reverse=True)
        return str(int(ary[0]['id']) + 1)

@app.route("/todos")
def index():
    res = table.scan()
    return jsonify(res['Items'])

@app.route("/todos/<id>")
def show(id):
    todo = get_todo(id)
    return jsonify(todo)

@app.route("/todos", methods=["POST"])
def create():
    title = request.json.get('title')
    if not title:
        return jsonify({'error': 'Please provider todo title'}), 422
    new_todo = { 'id': new_id(), 'title': title }
    res = table.put_item(Item=new_todo)
    return jsonify(new_todo), 201

@app.route("/todos/<id>", methods=["PUT"])
def update(id):
    edit_todo = get_todo(id)
    title = request.json.get('title')
    if not title:
        return jsonify({'error': 'Please provider todo title'}), 422
    table.update_item(
        Key={ 'id': edit_todo['id'] },
        UpdateExpression="set title = :n",
        ExpressionAttributeValues={ ':n': title }
    )
    return jsonify(get_todo(id)), 201

@app.route("/todos/<id>", methods=["DELETE"])
def destroy(id):
    todo = get_todo(id)
    res = table.delete_item(Key={ 'id': todo['id'] })
    return jsonify({'success': True}), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
