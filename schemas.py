from flask_marshmallow import Marshmallow

ma = Marshmallow()

class AlumnSchema(ma.Schema):
    class Meta:
        fields = ('id','name','surnames','classroom_id','date_of_birth')
        
class ClassroomSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'capacity')
        #con esta opcion mostrariamos tambien los alumnos de la clase
        #fields = ('id', 'name', 'capacity','alumns')
    #alumns = ma.Nested(AlumnSchema,many = True)
