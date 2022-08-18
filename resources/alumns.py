from flask import request, jsonify, Blueprint
from models import *
from schemas import *


alumn_bp = Blueprint('routes-alumns',__name__)

alumn_schema = AlumnSchema()
alumns_schema = AlumnSchema(many = True)

#CREATE A NEW ALUMN IN THE CLASSROOM REQUIRED
@alumn_bp.route('/classrooms/<id>/alumns',methods=['POST'])
def create_alumn(id):
    name = request.json['name']
    surnames = request.json['surnames']
    date_of_birth = request.json['date_of_birth']
    new_alumn = Alumn(name,surnames,id,date_of_birth)
    db.session.add(new_alumn)
    db.session.commit()
    return alumn_schema.jsonify(new_alumn)

#GET THE ALUMN REQUIRED BY ID
@alumn_bp.route('/classrooms/alumns/<id_a>',methods=['GET'])
def get_alumn(id_a):
    alumn = Alumn.query.get(id_a)
    return alumn_schema.jsonify(alumn)

#UPDATE THE ALUMN REQUIRED BY ID
@alumn_bp.route('/classrooms/alumns/<id_a>',methods = ['PUT'])
def update_alumn(id_a):

    alumn = Alumn.query.get(id_a)
    name = request.json['name']
    surnames = request.json['surnames']
    classroom_id = request.json['classroom']
    if Classroom.query.get(classroom_id) == None:
        return jsonify({"message":"Classroom not found"}),401
    alumn.name = name
    alumn.surnames = surnames
    alumn.classroom_id = classroom_id
    db.session.commit()
    return alumn_schema.jsonify(alumn)

#DELETE THE ALUMN REQUIRED BY ID
@alumn_bp.route('/classrooms/alumns/<id>',methods =['DELETE'])
def delete_alumn(id):
    alumn = Alumn.query.get(id)
    db.session.delete(alumn)
    db.session.commit()
    return alumn_schema.jsonify(alumn)

#GET ALL ALUMNS IN ANY CLASSROOM
@alumn_bp.route('/classrooms/alumns',methods = ['GET'])
def get_alumns():
    
    limit =request.args.get('limit')
    page = request.args.get('page')
    if limit != None and page != None:
        alumns = Alumn.query.paginate(page = int(page),per_page = int(limit))
        alumns = alumns.items
        return alumns_schema.jsonify(alumns)
    else:
        alumns = Alumn.query.all()
        return alumns_schema.jsonify(alumns)

    