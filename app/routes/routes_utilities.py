from flask import abort, make_response
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except ValueError:
        invalid_response = {{"message": f"This {cls.__name__} ID {model_id} is invalid"}}
        abort(make_response(invalid_response, 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"This {cls.__name__} with id {model_id} is not found"}
        abort(make_response(response, 404))
       
    return model