from AppFolder.Model.UsersModel import Users,user_schema,users_schema
from AppFolder import app,db
from flask import request, jsonify

# Create a User
@app.route('/user', methods=['POST'])
def add_user():
	username = request.json['username']
	email = request.json['email']
	password = request.json['password']
	new_users = Users(username, email, password)
	db.session.add(new_users)
	db.session.commit()
	return user_schema.jsonify(new_users)

# Get User
@app.route('/user/<email>', methods=['GET'])
def get_user(email):
	user = Users.query.filter_by(email=email).first()
	if user:
		return user_schema.jsonify(user)
	else:
		return '<h1>This user does not exist</h1>'

#Get all users
@app.route('/users', methods=['GET'])
def get_users():
	all_users = Users.query.all()
	result = users_schema.dump(all_users)
	return jsonify(result.data)

# Update a user
@app.route('/user/<email>', methods=['PUT'])
def update_user(email):
	user = Users.query.filter_by(email=email).first()
	if user:
		username = request.json['username']
		email = request.json['email']
		password = request.json['password']
		user.username = username
		user.email = email
		user.password = password
		db.session.commit()
		return user_schema.jsonify(user)
	else:
		return '<h1>This user does not exist</h1>'


# Delete User
@app.route('/user/<email>', methods=['DELETE'])
def delete_product(email):
	user = Users.query.filter_by(email=email).first()
	if user:
		db.session.delete(user)
		db.session.commit()
		return user_schema.jsonify(user)
	else:
		return '<h1>This user does not exist</h1>'
