from flask import Flask, request, jsonify
import pymysql

import yaml
with open('db_cfg.yaml', 'r') as infile:
    db_cfg = yaml.safe_load(infile)

db = pymysql.connect("localhost", "root", db_cfg['password'], "HackQuarantine")
#db = pymysql.connect("localhost", "username", "password", "database")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>SquadGoals API</h1>
<p>Retrieving data from the SquadGoals app. </p>'''

# --------------- Users --------------------------
@app.route('/api/v1/users/all', methods=['GET'])
def users_all():
    cursor = db.cursor()
    cursor.execute("select * from Users;")
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/api/v1/users', methods=['GET'])
def users_filter():
    query_parameters = request.args # Return query parameters used

    # Find user using id or username
    id = query_parameters.get('id')
    username = query_parameters.get('username')

    query = "select UserID, username, description from Users where"
    to_filter = []

    # Constructs query
    if id: # runs if it is not null
        query += ' UserID=%s AND'
        to_filter.append(id)
    if username:
        query += ' username=%s AND'
        to_filter.append(username)
    if not (id or username):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    # Executes query
    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()

    return jsonify(results)

# Find squads of a particular user
# Example call: http://127.0.0.1:5000/api/v1/users/squads?username=%22Brittame%22
@app.route('/api/v1/users/squads', methods=['GET'])
def users_squads():
    query_parameters = request.args # Return query parameters used

    # Find user using id or username
    id = query_parameters.get('id')
    username = query_parameters.get('username')

    query = "select u.UserID, u.username, s.SquadID, s.name, \
    s.description from Users_Squads us, Squads s, Users u where \
    u.UserID=us.userID and s.SquadID=us.squadID and"
    to_filter = []

    # Constructs query
    if id: # runs if it is not null
        query += ' u.UserID=%s AND'
        to_filter.append(id)
    if username:
        query += ' u.username=%s AND'
        to_filter.append(username)
    if not (id or username):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    # Executes query
    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()

    return jsonify(results)

# Find goals of a particular user
@app.route('/api/v1/users/goals', methods=['GET'])
def users_goals():
    query_parameters = request.args # Return query parameters used

    # Find user using id or username
    id = query_parameters.get('id')
    username = query_parameters.get('username')

    query = "select u.UserID, u.username, g.GoalID, g.name, g.description \
    from Users_Goals ug, Users u, Goals g where  u.UserID=ug.userID and \
    g.GoalID=ug.goalID and"
    to_filter = []

    # Constructs query
    if id: # runs if it is not null
        query += ' u.UserID=%s AND'
        to_filter.append(id)
    if username:
        query += ' u.username=%s AND'
        to_filter.append(username)
    if not (id or username):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    # Executes query
    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()

    return jsonify(results)


# Create a new user (using username and password)
@app.route('/api/v1/users/create', methods=['GET'])
def create_users():
    query_parameters = request.args
    username = query_parameters.get('username')
    password = query_parameters.get('password')
    description = query_parameters.get('description')

    # Check if username is unique
    uniqueQuery = "select exists(select username from Users where username={});".format(username)
    cursor = db.cursor()
    cursor.execute(uniqueQuery)
    results=cursor.fetchall()
    if results[0][0]==1:
        return "Username is already taken!"
    elif not (description):
        query = "insert into Users(username, password) values \
        ({},{});".format(username, password)
        cursor.execute(query)
        return "User created!"
    elif not (username or password):
        return page_not_found(404)
    else:
        query = "insert into Users(username, password, description) values \
        ({},{},{});".format(username, password, description)
        cursor.execute(query)
        return "User created!"

#/api/v1/users/create?username="Ed"&password="Duck"&description="I enjoy fishing"

# Delete a user
@app.route('/api/v1/users/delete', methods=['GET', 'POST'])
def delete_users():
    query_parameters = request.args
    # Find user using id or username
    id = query_parameters.get('id')
    username = query_parameters.get('username')

    query = "delete from Users where"
    to_filter = []

    # Constructs query
    if id: # runs if it is not null
        query += ' UserID=%s AND'
        to_filter.append(id)
    if username:
        query += ' username=%s AND'
        to_filter.append(username)
    if not (id or username):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    # Executes query
    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return "User deleted!"

# --------------- Friends --------------------------
# Find all the friends of a particular user
@app.route('/api/v1/users/friends', methods=['GET'])
def users_friends():
    query_parameters = request.args # Return query parameters used

    # Find user using id or username
    id = query_parameters.get('id')
    username = query_parameters.get('username')

    query = "select u1.UserID, u1.username, u2.UserID, u2.username, \
    f.friendshipDate from Friends f, Users u1, Users u2 where \
    u1.UserID=f.userID1 and u2.UserID=f.userID2 and"
    to_filter = []

    # Constructs query
    if id: # runs if it is not null
        query += ' (u1.UserID=%s or u2.UserID=%s) AND'
        to_filter.append(id)
        to_filter.append(id)
    if username:
        query += ' (u1.username=%s or u2.username=%s) AND'
        to_filter.append(username)
        to_filter.append(username)
    if not (id or username):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    # Executes query
    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()

    return jsonify(results)

# --------------- Squads --------------------------
@app.route('/api/v1/squads/all', methods=['GET'])
def squads_all():
    cursor = db.cursor()
    cursor.execute("select * from Squads;")
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/api/v1/squads', methods=['GET'])
def squads_filter():
    query_parameters = request.args

    # Find squad using SquadID or name (although name is not unique)
    id = query_parameters.get('id')
    name = query_parameters.get('name')

    query = "select * from Squads where"
    to_filter = []
    if id:
        query += ' SquadID=%s AND'
        to_filter.append(id)
    if name:
        query += ' name=%s AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return jsonify(results)

# Find users of a squad through SquadID or name
@app.route('/api/v1/squads/users', methods=['GET'])
def squads_users():
    query_parameters = request.args

    # Find squad using SquadID or name (although name is not unique)
    id = query_parameters.get('id')
    name = query_parameters.get('name')

    query = "select u.UserID, u.username, s.SquadID, s.name \
     from Users_Squads us, Squads s, Users u where \
    u.UserID=us.userID and s.SquadID=us.squadID and"
    to_filter = []
    if id:
        query += ' s.SquadID=%s AND'
        to_filter.append(id)
    if name:
        query += ' s.name=%s AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return jsonify(results)

# Find goals of a squad
@app.route('/api/v1/squads/goals', methods=['GET'])
def squads_goals():
    query_parameters = request.args
    id = query_parameters.get('id')
    name = query_parameters.get('name')

    query = "select g.GoalID, g.name, g.description, s.SquadID, s.name, \
    s.description from Squads_Goals sg, Squads s, Goals g where \
    s.SquadID=sg.squadID and g.GoalID=sg.goalID and"
    to_filter = []
    if id:
        query += ' s.SquadID=%s AND'
        to_filter.append(id)
    if name:
        query += ' s.name=%s AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return jsonify(results)

# --------------- Goals --------------------------
@app.route('/api/v1/goals/all', methods=['GET'])
def goals_all():
    cursor = db.cursor()
    cursor.execute("select * from Goals;")
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/api/v1/goals', methods=['GET'])
def goals_filter():
    query_parameters = request.args

    # Find goal using GoalID or name (although name is not unique)
    id = query_parameters.get('id')
    name = query_parameters.get('name')
    query = "select * from Goals where"
    to_filter = []
    if id:
        query += ' GoalID=%s AND'
        to_filter.append(id)
    if name:
        query += ' name=%s AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return jsonify(results)


# Find squads relating to a goal
@app.route('/api/v1/goals/squads', methods=['GET'])
def goals_squads():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')
    query = "select g.GoalID, g.name, g.description, s.SquadID, s.name, \
    s.description from Squads_Goals sg, Squads s, Goals g where \
    s.SquadID=sg.squadID and g.GoalID=sg.goalID and"
    to_filter = []
    if id:
        query += ' g.GoalID=%s AND'
        to_filter.append(id)
    if name:
        query += ' g.name=%s AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return jsonify(results)

# Finds all users of a particular goal
@app.route('/api/v1/goals/users', methods=['GET'])
def goals_users():
    query_parameters = request.args

    id = query_parameters.get('id')
    name = query_parameters.get('name')
    query = "select u.UserID, u.username, g.GoalID, g.name, g.description \
    from Users_Goals ug, Users u, Goals g where  u.UserID=ug.userID and \
    g.GoalID=ug.goalID and"
    to_filter = []
    if id:
        query += ' g.GoalID=%s AND'
        to_filter.append(id)
    if name:
        query += ' g.name=%s AND'
        to_filter.append(name)
    if not (id or name):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return jsonify(results)

# --------------- Goal updates --------------------------
@app.route('/api/v1/goals/updates/all', methods=['GET'])
def goal_updates_all():
    cursor = db.cursor()
    cursor.execute("select * from Goal_Updates;")
    results = cursor.fetchall()
    return jsonify(results)

@app.route('/api/v1/goals/updates', methods=['GET'])
def goal_updates_filter():
    query_parameters = request.args

    # Find updates using UpdateID or GoalID (although name is not unique)
    UpdateID = query_parameters.get('UpdateID')
    GoalID = query_parameters.get('GoalID')
    query = "select * from Goal_Updates where"
    to_filter = []
    if UpdateID:
        query += ' UpdateID=%s AND'
        to_filter.append(UpdateID)
    if GoalID:
        query += ' goalID=%s AND'
        to_filter.append(GoalID)
    if not (UpdateID or GoalID):
        return page_not_found(404)
    query = query[:-4] + ';'
    query_str = query % tuple(to_filter)

    cursor = db.cursor()
    cursor.execute(query_str)
    results = cursor.fetchall()
    return jsonify(results)

# -----------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Not found'})

if __name__ == '__main__':
    app.run(debug=True)
