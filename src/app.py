"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
         #"hello": "world",
         "family": members
    }
    return jsonify(response_body['family']), 200

# aca voy a agregar una ruta para traer un solo miembro

@app.route('/member/<int:id>', methods=["GET"])
def get_single_member(id):
    member = jackson_family.get_member(id)

    if (member != None and member != {}):

        return jsonify(member), 200
    else:
        return jsonify({'message': 'No se encontro ese usuario'}), 400

# ahora necesito agregar gente  

@app.route('/member', methods=['POST'])
def create_member():
    body = json.loads(request.data)

    if (body['age'] > 0 and type(body['lucky_numbers']) == list and type(body['first_name']) == str):
        #body['id'] = jackson_family._generateId() esta linea era para agregar un id aleatorio pero la test le mete el suyo a webo asi que lo quite para que no de error
        jackson_family.add_member(body)
        return jsonify({'message': 'miembro agregado'}), 200
    else:
        return jsonify({'message': 'alguno de los campos esta mal'}), 400

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_members(member_id):
    was_delete = jackson_family.delete_member(member_id)
    if was_delete == True:
        response_body = {  # este response body lo hice por las test, yo habia puesto un mensaje que decia: has sido exculmulgado perro!!!
            'done': True
        }
        return jsonify(response_body), 200
    else:
        return jsonify({'message': 'no se pudo eliminar esa persona'}), 400

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
