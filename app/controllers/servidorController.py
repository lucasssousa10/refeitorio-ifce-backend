from app import app, db, Messages
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from sqlalchemy import exc
from werkzeug.security import generate_password_hash
from . import resource
from app import Servidor
from app import ServidorValidator
from app import fieldsFormatter



@app.route("/servidor/add", methods=["POST"])
@jwt_required
@resource("servidor-add")
def servidorAdd():
    data = request.get_json()
    validator = ServidorValidator(data)
    
    errors = validator.validate()

    if errors["has"]:
        return (
            jsonify(
                {
                    "message": Messages.FORM_VALIDATION_ERROR,
                    "error": errors["has"],
                    "errors": errors,
                }
            ),
            200,
        )

    servidor = Servidor(
        cpf = data['cpf'],
        siape = data['siape'],
        nome = data['nome'], 
        users_id = data['users_id']
    )

    db.session.add(servidor)

    try:
        db.session.commit()
        return jsonify(
            {
                "message": Messages.REGISTER_SUCCESS_CREATED.format("Servidor"),
                "error": False,
            }
        )
    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(
            {"message": Messages.REGISTER_CREATE_INTEGRITY_ERROR, "error": True}
        )

