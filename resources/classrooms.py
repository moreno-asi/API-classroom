from flask import request, jsonify, Blueprint
from models import *
from schemas import *

classroom_bp = Blueprint('routes-classrooms',__name__)

classroom_schema = ClassroomSchema()
classrooms_schema = ClassroomSchema(many=True)


#INSERT A NEW CLASSROOM
@classroom_bp.route('/classrooms', methods=['Post'])
def create_classroom():
  
  name = request.json['name']
  capacity = request.json['capacity']
  if Classroom.query.filter_by(name = name).first() != None:
    return jsonify({"message":"Error Classroom name "}),401
  new_classroom= Classroom(name, capacity)

  db.session.add(new_classroom)
  db.session.commit()

  return classroom_schema.jsonify(new_classroom)

#GET ALL CLASSROOMS
@classroom_bp.route('/classrooms', methods=['GET'])
def get_classrooms():
  all_classrooms = Classroom.query.all()
  result = classrooms_schema.dump(all_classrooms)
  return jsonify(result)

#GET CLASSROOM WITH ID REQUIRED
@classroom_bp.route('/classrooms/<id>', methods=['GET'])
def get_classroom(id):
  classroom = Classroom.query.get(id)
  return classroom_schema.jsonify(classroom)

#UPDATE CLASSROOM WITH ID REQUIRED
@classroom_bp.route('/classrooms/<id>', methods=['PUT'])
def update_classroom(id):
  classroom = Classroom.query.get(id)

  name = request.json['name']
  capacity = request.json['capacity']

  classroom.name = name
  classroom.capacity = capacity

  db.session.commit()

  return classroom_schema.jsonify(classroom),200

#DELETE CLASSROOM WITH ID REQUIRED
@classroom_bp.route('/classrooms/<id>', methods=['DELETE'])
def delete_classrom(id):
  classroom = Classroom.query.get(id)
  db.session.delete(classroom)
  db.session.commit()
  return classroom_schema.jsonify(classroom)

############################################################################################



@classroom_bp.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Welcome to my API'})