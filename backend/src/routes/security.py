from flask import Blueprint , jsonify, request
import uuid
#Entities
from models.entities.seguridad import persona, usuario

# models
from models.security_model import SeguridadModel

main=Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_usuario():
    try:
        usuarios=SeguridadModel.get_usuario()
        return jsonify(usuarios)
    except Exception as ex:

        return jsonify({'message':str(ex)}),500

@main.route('/<id>')  
def get_user(id):
    try:
        user=SeguridadModel.get_user(id)
        if user !=  None: 
            return jsonify(user)
        else:
            return jsonify({}),400
    except Exception as ex:
        return jsonify({'message' : str(ex)}),500
    
@main.route('/add',methods=['POST'])  
def add_persona():
    try:
        Dni = request.json['dni']
        Primer_nombre = request.json['primer_nombre']
        Segundo_nombre = request.json['segundo_nombre']
        Primer_apellido =request.json['primer_apellido']
        Segundo_apellido =request.json['segundo_apellido']
        Celular =request.json['celular']
        Cod_uni = request.json['codigo_uni']
        Correo_uni =request.json['correo_uni']
        Contrasena= request.json['contrasena']
        
        person=persona(Dni,Primer_nombre,Segundo_nombre,Primer_apellido,Segundo_apellido,Celular)
        
        user = usuario(None,Dni=Dni, Cod_uni=Cod_uni, Correo_uni=Correo_uni, Contrasena=Contrasena)

        affected_rows=SeguridadModel.add_person(person,user)   
        print(affected_rows)

        if affected_rows == -1 :
            return jsonify(person.dni)
        else:
            return jsonify({'message': "Error en insert"}),500
        

        return jsonify({})

    except Exception as ex:
        return jsonify({'message' : str(ex)}),500
    

@main.route('/login',methods=['GET','POST'])  
def login():
    try:
        correo_uni= request.json['correo_uni']
        contrasena= request.json['contrasena']
        user=usuario(None,None,None,correo_uni,contrasena)
        session=SeguridadModel.login(user)

        if session : 
            return jsonify(correo_uni)
        else:
            return jsonify({'Message':'No inicio session'})
        
        return jsonify({})

           
    except Exception as ex:
        return jsonify({'message' : str(ex)}),500