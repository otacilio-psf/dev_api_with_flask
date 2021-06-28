from flask_restful     import Resource
from flask             import request
from flask_httpauth    import HTTPBasicAuth
from werkzeug.security import check_password_hash
from src.models        import Developers_model


auth = HTTPBasicAuth()

@auth.verify_password
def verify(user, password):
    if not (user, password):
        return False
    user_pass = Users.query.filter_by(user=user, active=1).first()
    if not user_pass:
        return False
    return check_password_hash(user_pass.password, password)

class Developers(Resource):

    def get(self):
        devs = Developers_model.query.all()
        response = []
        try:
            for dev in devs:  
                r = {
                    'id': dev.id,
                    'name': dev.name,
                    'age': dev.age,
                    'email': dev.email
                }
                response.append(r)
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response
    
    @auth.login_required
    def post(self):
        b_data = request.json
        try:
            dev = Developers_model(name=b_data["name"], age=b_data["age"], email=b_data["email"])
            dev.save()
            response = {
                    'id': dev.id,
                    'name': dev.name,
                    'age': dev.age,
                    'email': dev.email
                }
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response
        

class Developer(Resource):

    def get(self, id):
        dev = Developers_model.query.filter_by(id=id).first()
        try:
            response = {
                'id': dev.id,
                'name': dev.name,
                'age': dev.age,
                'email': dev.email
            }
        except AttributeError:
            response = {
                "status": "Error",
                "menssage": f"Id: {id} doesn't exist"
            }
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response
    
    @auth.login_required
    def put(self, id):
        dev = Developers_model.query.filter_by(id=id).first()
        b_data = request.json
        try:
            if "name" in b_data:
                dev.name = b_data["name"]
            if "age" in b_data:
                dev.age = b_data["age"]
            if "email" in b_data:
                dev.email = b_data["email"]
            dev.save()
            response = {
                'id': dev.id,
                'name': dev.name,
                'age': dev.age,
                'email': dev.email
            }
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response

    @auth.login_required
    def delete(self, id):
        dev = Developers_model.query.filter_by(id=id).first()
        try:
            dev.delete()
            response = {
                "status": "sucess",
                "menssage": f"Delete ID {id} Sucessful"
            }
        except Exception as e:
            response = {
                "status": "Error",
                "menssage": f"Error: {e}"
            }
        return response