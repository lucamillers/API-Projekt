
"""
Example script showing how to represent todo lists and todo entries in Python
data structures and how to implement endpoint for a REST API with Flask.

Requirements:
* flask
"""

import uuid

from flask import Flask, request, jsonify, abort


# initialize Flask server
app = Flask(__name__)

# create unique id for lists, users, entries
user_id_bob = str(uuid.uuid4())
user_id_alice = str(uuid.uuid4())
user_id_eve = str(uuid.uuid4())
todo_list_1_id = '1318d3d1-d979-47e1-a225-dab1751dbe75'
todo_list_2_id = '3062dc25-6b80-4315-bb1d-a7c86b014c65'
todo_list_3_id = '44b02e00-03bc-451d-8d01-0c67ea866fee'
todo_1_id = str(uuid.uuid4())
todo_2_id = str(uuid.uuid4())
todo_3_id = str(uuid.uuid4())
todo_4_id = str(uuid.uuid4())

# define internal data structures with example data
user_list = [
    {'id': user_id_bob, 'name': 'Bob'},
    {'id': user_id_alice, 'name': 'Alice'},
    {'id': user_id_eve, 'name': 'Eve'},
]
todo_lists = [
    {'id': todo_list_1_id, 'name': 'Einkaufsliste'},
    {'id': todo_list_2_id, 'name': 'Arbeit'},
    {'id': todo_list_3_id, 'name': 'Privat'},
]
todos = [
    {'id': todo_1_id, 'name': 'Milch', 'description': '', 'list': todo_list_1_id, 'user': user_id_bob},
    {'id': todo_2_id, 'name': 'Arbeitsblätter ausdrucken', 'description': '', 'list': todo_list_2_id, 'user': user_id_alice},
    {'id': todo_3_id, 'name': 'Kinokarten kaufen', 'description': '', 'list': todo_list_3_id, 'user': user_id_eve},
    {'id': todo_3_id, 'name': 'Eier', 'description': '', 'list': todo_list_1_id, 'user': user_id_eve},
]


# add some headers to allow cross origin access to the API on this server, necessary for using preview in Swagger Editor!
@app.after_request
def apply_cors_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

# define endpoint for getting and deleting existing todo lists
@app.route('/list/<list_id>', methods=['GET', 'DELETE'])
def handle_list(list_id):
    # find todo list depending on given list id
    list_item = None
    for l in todo_lists:
        if l['id'] == list_id:
            list_item = l
            break
    # if the given list id is invalid, return status code 404
    if not list_item:
        abort(404)
    if request.method == 'GET':
        # find all todo entries for the todo list with the given id
        print('Returning todo list...')
        return jsonify([i for i in todos if i['list'] == list_id])
    elif request.method == 'DELETE':
        # delete list with given id
        print('Deleting todo list...')
        todo_lists.remove(list_item)
        return '', 200

# define endpoint for getting and deleting existing todo list entries
@app.route('/list/<list_id>/entry', methods=['POST'])
def add_new_entry(list_id):
    if request.method == 'POST':
    # make JSON from POST data (even if content type is not set correctly)
        new_entry = request.get_json(force=True)
        print('Got new entry to be added: {}'.format(new_entry))
    # create id for new entry, save it and return the list with id
        new_entry['id'] = str(uuid.uuid4())
        new_entry['list'] = list_id
        todos.append(new_entry)
        print('Current Entries: {}'.format(todos))
        return jsonify(new_entry), 200

# define endpoint for updating existing todo list entries
@app.route('/list/<list_id>/entry/<entry_id>', methods=['POST', 'DELETE'])
def handle_entry(list_id, entry_id):
    # find todo list depending on given list id
    list_item = None
    for l in todo_lists:
        if l['id'] == list_id:
            list_item = l
            break
    # find todo list entry depending on given entry id
    entry_item = None
    for g in todos:
        if g['id'] == entry_id:
            entry_item = g
            break
    # if the given list id is invalid, return status code 404
    if not list_item:
        abort(404)
    elif not list_item:
        abort(404)
    # if the given entry id is invalid, return status code 404
    if not entry_item:
        abort(404)
    elif not entry_item:
        abort(404)
    if request.method == 'POST':
        # delete list entry with given id
        print('Deleting item from list...')
        todos.remove(entry_item)
        # make JSON from POST data (even if content type is not set correctly)
        new_entry = request.get_json(force=True)
        print('Got new entry to be added: {}'.format(new_entry))
        # create id for new entry, save it and return the list with id (thus updating an existing entry)
        new_entry['id'] = str(uuid.uuid4())
        new_entry['list'] = list_id
        todos.append(new_entry)
        print('Current Entries: {}'.format(todos))
        return jsonify(new_entry), 200
    elif request.method == 'DELETE':
        # delete list entry with given id
        print('Deleting item from list...')
        todos.remove(entry_item)
        return jsonify(todos), 200

# define endpoint for adding a new list
@app.route('/list', methods=['POST'])
def add_new_list():
    # make JSON from POST data (even if content type is not set correctly)
    new_list = request.get_json(force=True)
    print('Got new list to be added: {}'.format(new_list))
    # create id for new list, save it and return the list with id
    new_list['id'] = str(uuid.uuid4())
    todo_lists.append(new_list)
    print('Current Lists: {}'.format(todo_lists))
    return jsonify(new_list), 200

# define endpoint for getting all lists
@app.route('/lists', methods=['GET'])
def get_all_lists():
    return jsonify(todo_lists)

# define endpoint for getting all users
@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(user_list)

# define endpoint for getting all todos
@app.route('/todos', methods=['GET'])
def get_all_todos():
    return jsonify(todos) 

# define endpoint for adding a new list
@app.route('/user', methods=['POST'])
def add_new_user():
    # make JSON from POST data (even if content type is not set correctly)
    new_user = request.get_json(force=True)
    print('Got new user to be added: {}'.format(new_user))
    # create id for new list, save it and return the list with id
    new_user['id'] = str(uuid.uuid4())
    user_list.append(new_user)
    print('Current Users: {}'.format(user_list))
    return jsonify(user_list), 200

@app.route('/user/<user_id>', methods=['GET', 'DELETE'])
def handle_user(user_id):
    # find todo list depending on given list id
    user_item = None
    for l in user_list:
        if l['id'] == user_id:
            user_item = l
            break
    # if the given list id is invalid, return status code 404
    if not user_item:
        abort(404)
    if request.method == 'GET':
        # find all todo entries for the todo list with the given id
        print('Returning user list...')
        return jsonify([i for i in user_list if i['id'] == user_id])
    elif request.method == 'DELETE':
        # delete list with given id
        print('Deleting user from list...')
        user_list.remove(user_item)
        return jsonify(user_list), 200


if __name__ == '__main__':
    # start Flask server
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
